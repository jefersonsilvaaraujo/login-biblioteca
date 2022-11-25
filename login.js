const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({ headless: false });
  const page = await browser.newPage();
  //Acessa a pagina de login da biblioteca
  await page.goto('https://dliportal.zbra.com.br/Login.aspx?key=ESUP');
  
  //Clica no botao para aceitar todos os cookies
  await page.click('[class="cookies-policy-accept-button"]');

  //Insere os dados de login
  await page.type('[name="userIdTextBox"]', '1400206163');
  await page.type('[name="passwordTextBox"]', 'Aluno@esup');

  //Clica no botao de login
  await page.click('[name="loginButton"]');

})();