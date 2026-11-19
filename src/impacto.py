from datetime import date

import database as db

FATOR_KG = {"kg": 1.0, "g": 0.001}


def classificar_urgencia(prazo, hoje):
    if not prazo:
        return "BAIXA"
    dias = (date.fromisoformat(str(prazo)[:10]) - hoje).days
    if dias <= 0:
        return "ALTA"
    if dias == 1:
        return "MÉDIA"
    return "BAIXA"


def registrar_impacto(protocolo, extrator):
    doacao = db.buscar_doacao_por_protocolo(protocolo)
    if not doacao:
        return []
    prazo = doacao.get("data_validade") or extrator.extrair_validade(
        doacao.get("mensagem_original") or "", resposta_direta=True)["data_validade"]
    urgencia = classificar_urgencia(prazo, extrator._agora().date())
    validade = str(doacao["data_validade"])[:10] if doacao.get("data_validade") else "não informada"
    primeira = next((m for m in doacao["matches"] if m["ordem"] == 1), None)
    ong_destino = primeira["ong_nome"] if primeira else "Sem ONG compatível"
    registros = []
    for item in doacao["itens"]:
        fator = FATOR_KG.get(item.get("unidade"))
        if fator is None or item.get("quantidade") is None:
            continue
        registro = {"alimento": str(item["alimento"]).strip().capitalize(),
                    "quantidade_kg": round(float(item["quantidade"]) * fator, 3),
                    "validade": validade, "urgencia": urgencia, "ong_destino": ong_destino}
        db.registrar_doacao_impacto(**registro)
        registros.append(registro)
    return registros
