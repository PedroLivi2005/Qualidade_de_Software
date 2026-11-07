from playwright.sync_api import Page, expect

# Responsável: Pedro Guterres Jaeger Livi

def test_entrar_no_sistema(page: Page):
    # Arrange: Acessa a página de login do LocalEats
    page.goto("https://local-eats-unisenac.vercel.app/static/login.html")

    # Act: Preenche as credenciais e clica no botão de entrar do formulário
    page.get_by_placeholder("teste@teste.com").fill("pedro.livi@email.com")
    page.get_by_placeholder("Sua senha secreta").fill("570zd")
    
    # Seleciona especificamente o botão de submit do formulário para evitar ambiguidade
    page.locator("#loginForm").get_by_role("button", name="Entrar").click()

    # Assert 1: Verifica se a URL foi alterada após o login bem-sucedido
    expect(page).not_to_have_url("https://local-eats-unisenac.vercel.app/static/login.html")

    # Assert 2: Verifica se a interface pós-login está visível
    expect(page.locator("body")).to_be_visible()