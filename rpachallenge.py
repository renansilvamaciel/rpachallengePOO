from webdriver_manager.chrome import ChromeDriverManager
from botcity.web.browsers.chrome import default_options
from botcity.web import WebBot, By
import config
from pastas_arquivos import PastasArquivos


class RpaChallenge():
    def __init__(self):
        self.bot = WebBot()
        self._desafio = None
        self._nome = None
        self.folder = PastasArquivos()

    @property
    def desafio(self):
        return self._desafio

    @desafio.setter
    def desafio(self, desafio: str):
        self._desafio = desafio

    def login(self) -> None:
        """
        Acesso o portal do RPA Challenge.

        """
        try:
            # Instalar o driver no objeto do bot
            self.bot.driver_path = ChromeDriverManager().install()

            # Configurações iniciais
            self.bot.download_folder_path = config.resources_folder
            def_options = default_options(download_folder_path=config.resources_folder)
            self.bot.options = def_options

            # Navega para o site
            self.bot.navigate_to("https://www.rpachallenge.com/")

            # Maximizar a tela do google chrome
            self.bot.maximize_window()

            # Conferir se a tela carregou com sucesso
            if not self.bot.find_element("//button[text()='Start']", By.XPATH, ensure_visible=True):
                raise Exception('Falha ao validar carregamento do desafio input forms')

        except Exception as error:
            # TODO: Buscar outras infomações sobre os erros.
            raise ValueError(error)


    def escolher_desafio(self) -> None:
        """
        Escolher o safio a ser feito no site do RPA Challenge
        """
        try:

            # Selecionar o desafio
            self.bot.find_element(f"//a[text()='{self._desafio}']", By.XPATH, ensure_visible=True)


        except Exception as error:

            # TODO: Buscar outras informações sobre os erros.
            # ideias: passar todas as informações de erro por uma string e fazer o eval na orquestradora.
            raise ValueError(error)


    def baixar_csv_input_forms(self) -> str:
        """
        Baixa o arquivo CSV do desafio input forms, e guarda na pasta de recursos.

        """
        try:
            # Clicar em baixar o arquivo CSV
            self.bot.find_element(selector="//div[a[contains(text(),'Download Excel')]]",
                                  by=By.XPATH,
                                  ensure_visible=True,
                                  ensure_clickable=True).click()

            arquivo = self.folder.aguardar_conclusao_download(extensao_arquivo='.xlsx')

            return arquivo

        except Exception as error:

            # TODO: Buscar outras informações sobre os erros.
            raise ValueError(error)



    def iniciar_desafio(self):
        try:
            ...
        except Exception as error:
            raise ValueError(error)

