from botcity.web import WebBot, Browser

class Bot(WebBot):
    def action(self, execution=None):
        # self.headless false= o navegador abrirá visivelmente,
        # true= ele executará o programa em segundo plano
        self.headless = False


        self.driver_path = "./chromedriver.exe"

        # Opens the BotCity website.
        self.browse("https://www.google.com.br/")
        
        if not self.find( "lupa", matching=0.97, waiting_time=10000):
            self.not_found("lupa")
        self.click()
        
        
        self.paste("cotação dolar")
        self.enter()
        
        if not self.find( "dolar", matching=0.97, waiting_time=10000):
            self.not_found("dolar")
        self.double_click_relative(25, 51)
        
        self.control_c()
        cotacao = self.get_clipboard()
        print(cotacao)
        
        if not self.find( "fechar", matching=0.97, waiting_time=10000):
            self.not_found("fechar")
        self.click()
        self.paste("cotação euro")
        self.enter()       
        
        if not self.find( "euro", matching=0.97, waiting_time=10000):
            self.not_found("euro")
        self.double_click_relative(26, 48)
        
        self.control_c()
        cotacao = self.get_clipboard()
        print(cotacao)
                

        # Wait for 10 seconds before closing
        # self.wait(10000)

        # Stop the browser and clean up
        self.stop_browser()

    def not_found(self, label):
        print(f"Element not found: {label}")


if __name__ == '__main__':
    Bot.main()


