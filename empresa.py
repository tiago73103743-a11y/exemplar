class Empresa:
    def __init__(self):
        # Dados da empresa — edite aqui com as informações reais
        self.dados = {
            "nome": "Loja Exemplo Comércio e Serviços Ltda",
            "subtitulo": "Especialistas em soluções digitais para o seu negócio",
            "descricao": (
                "Somos uma empresa fundada com o propósito de oferecer produtos e serviços de qualidade, "
                "unindo tecnologia e confiança. Atuamos no mercado desde 2020, atendendo clientes em todo o Brasil "
                "com dedicação, transparência e inovação."
            ),
            "missao": "Proporcionar experiências de compra seguras, práticas e acessíveis, contribuindo para o crescimento dos nossos clientes.",
            "visao": "Ser referência nacional em e-commerce e soluções digitais até 2030, sempre com ética e sustentabilidade.",
            "valores": "Honestidade, qualidade, respeito ao cliente, responsabilidade social e inovação contínua.",
            "cnpj": "00.000.000/0001-00",
            "data_fundacao": "10/10/2020",
            "cidade_uf": "Belo Horizonte — MG",
            "email": "contato@lojaexemplo.com.br",
            "telefone": "(31) 99999-9999"
        }

    def exibir_resumo(self):
        """Exibe um resumo da empresa no terminal"""
        print("=" * 60)
        print(f"EMPRESA: {self.dados['nome']}")
        print("=" * 60)
        print(f"CNPJ: {self.dados['cnpj']}")
        print(f"Fundação: {self.dados['data_fundacao']}")
        print(f"Localização: {self.dados['cidade_uf']}")
        print(f"E-mail: {self.dados['email']}")
        print("\n--- SOBRE ---")
        print(self.dados['descricao'])
        print("\n--- MISSÃO ---")
        print(self.dados['missao'])
        print("\n--- VISÃO ---")
        print(self.dados['visao'])
        print("\n--- VALORES ---")
        print(self.dados['valores'])
        print("=" * 60)

    def gerar_html(self, arquivo_saida="sobre_empresa.html"):
        """Gera a página HTML completa com os dados da empresa"""
        html_conteudo = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sobre Nós — {self.dados['nome']}</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; font-family: sans-serif; }}
        body {{ background: #f5f7fa; padding: 2rem; line-height: 1.6; }}
        .caixa {{ max-width: 800px; margin: 0 auto; background: white; padding: 2.5rem; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}
        h1 {{ color: #2c3e50; text-align: center; margin-bottom: 0.5rem; }}
        .sub {{ text-align: center; color: #7f8c8d; margin-bottom: 2rem; }}
        h2 {{ color: #2980b9; margin: 1.5rem 0 0.5rem; font-size: 1.2rem; }}
        .linha {{ margin: 0.5rem 0; }}
        .dados {{ display: grid; grid-template-columns: 1fr 1fr; gap: 0.5rem; margin-top: 1rem; }}
        footer {{ text-align: center; margin-top: 2rem; color: #7f8c8d; font-size: 0.9rem; }}
        @media(max-width: 600px) {{ .dados {{ grid-template-columns: 1fr; }} }}
    </style>
</head>
<body>
    <div class="caixa">
        <h1>{self.dados['nome']}</h1>
        <p class="sub">{self.dados['subtitulo']}</p>

        <h2>Sobre Nós</h2>
        <p>{self.dados['descricao']}</p>

        <h2>Missão</h2>
        <p>{self.dados['missao']}</p>

        <h2>Visão</h2>
        <p>{self.dados['visao']}</p>

        <h2>Valores</h2>
        <p>{self.dados['valores']}</p>

        <h2>Contato e Identificação</h2>
        <div class="dados">
            <div class="linha"><strong>CNPJ:</strong> {self.dados['cnpj']}</div>
            <div class="linha"><strong>Fundação:</strong> {self.dados['data_fundacao']}</div>
            <div class="linha"><strong>Localização:</strong> {self.dados['cidade_uf']}</div>
            <div class="linha"><strong>E-mail:</strong> {self.dados['email']}</div>
        </div>
    </div>
    <footer>
        &copy; 2026 {self.dados['nome']} — Todos os direitos reservados
    </footer>
</body>
</html>"""
        with open(arquivo_saida, "w", encoding="utf-8") as f:
            f.write(html_conteudo)
        print(f"✅ Página '{arquivo_saida}' gerada com sucesso!")


# Execução
if __name__ == "__main__":
    minha_empresa = Empresa()
    
    # Exibe resumo no terminal
    minha_empresa.exibir_resumo()
    
    # Gera o arquivo HTML completo
    minha_empresa.gerar_html()