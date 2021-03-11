from django.db import models
from django.core.validators import  MinLengthValidator
from django.db import models
from django.utils import timezone
from django import forms
from django.http import HttpResponseRedirect, HttpResponse, request
from bootstrap_datepicker_plus import DatePickerInput

# Create your models here.

class Numero(models.Model):
        numero = models.CharField(
                max_length=40,
                help_text='O número do processo tem, geralmente, no mínimo 25 caracteres.',
                validators=[MinLengthValidator(25, "Preencha corretamente o número do Processo")]
    )
class Empresa(models.Model):
    name = models.CharField(
            max_length=200,
            help_text='Cadastre uma empresa (e.g. Uber).',
            validators=[MinLengthValidator(4, "O nome da empresa deve ser maior que 4 caracteres.")]
    )
    cnpj = models.CharField(
            max_length=18,
            help_text='O CNPJ dee conter 14 números.',
            validators=[MinLengthValidator(14, "O CNPJ deve conter 14 números")]
    )
    ano_rfb = models.DateField()


    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Tribunal(models.Model):
    name = models.CharField(
            max_length=200,
            help_text='Cadastre os Tribunais do Trabalho, Tribunal Superior do Trabalho, entre outros (e.g. TRT3)',
            unique = True,
            #validators=[MinLengthValidator(4, "O campo do tribunal deve possuir mais que 4 caracteres.")]
    )
    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Varas(models.Model):
    regiao = models.ForeignKey('Tribunal', on_delete=models.CASCADE, null = True, blank = True)
    name = models.CharField(
            max_length=200,
            help_text='Cadastre as Varas do Trabalho ou de outros Tribunais, como os Cíveis.',
            unique = True,
            validators=[MinLengthValidator(6, "Este campo deve possuir mais que 6 caracteres.")]
    )



    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Jurisdicao(models.Model):
    name = models.CharField(
            max_length=200,
            help_text='Cadastre as Jurisdições',
            unique = True,
            validators=[MinLengthValidator(5, "Este campo deve possuir mais que 5 caracteres.")]
    )
    varas = models.ForeignKey('Varas', on_delete=models.CASCADE, null = True)

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class TermoBusca(models.Model):
    name = models.CharField(
            max_length=200,
            help_text='Cadastre os termos buscados nas bases de dados',
            validators=[MinLengthValidator(4, "O campo do tribunal deve possuir mais que 4 caracteres.")]
    )

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Arquivo(models.Model):
    pass
    #def up(self):
        #title = models.CharField(max_length=50)
        #pdf = models.FileField()

    def __str__(self):
        return self.arquivo

def upload_arquivo(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES["document"]
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)

class AutoDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        return timezone.now()

#========== INSTÂNCIAS ==================

PRIMEIRA_INSTANCIA = '1ª Instância'
SEGUNDA_INSTANCIA = '2ª Instância'

GRAU = (
    ('PRIMEIRA_INSTANCIA', '1ª Instância'),
    ('SEGUNDA_INSTANCIA', '2ª Instância'),
    )


# TRIBUNAIS E VARAS DO TRABALHO ===================================

TRT1 = '1ª Região - Rio de Janeiro/RJ'
TRT2 = '2ª Região - São Paulo/SP'
TRT3 = '3ª Região - Belo Horizonte/MG'
TRT4 = '4ª Região - Porto Alegre/RS'
TRT5 = '5ª Região - Salvador/BA'
TRT6 = '6ª Região - Recife/PE'
TRT7 = '7ª Região - Fortaleza/CE'
TRT8 = '8ª Região - Belém/PA'
TRT9 = '9ª Região - Curitiba/PR'
TRT10 = '10ª Região - Brasília/DF - TO'
TRT11 =  '11ª Região - Manaus/AM - RR'
TRT12 = '12ª Região - Florianópolis/SC'
TRT13 = '13ª Região - João Pessoa/PB'
TRT14 = '14ª Região - Porto Velho/RO'
TRT15 = '15ª Região - Campinas'
TRT16 = '16ª Região - São Luís/MA'
TRT17 = '17ª Região - Vitória/ES'
TRT18 = '18ª Região - Goiânia/GO'
TRT19 = '19ª Região - Maceió/AL'
TRT20 = '20ª Região - Aracaju/SE'
TRT21 = '21ª Região - Natal/RN'
TRT22 = '22ª Região - Teresina/PI'
TRT23 = '23ª Região - Cuiabá/MT'
TRT24 = '24ª Região - Campo Grande/MS'
TST =  'TST -Tribunal Superior do Trabalho'

TRIBUNAIS_TRABALHISTAS = (
        (1, 'TRT1'),
        (2, 'TRT2'),
        (3, 'TRT3'),
        (4, 'TRT4'),
        (5, 'TRT5'),
        (6, 'TRT6'),
        (7, 'TRT7'),
        (8, 'TRT8'),
        (9, 'TRT9'),
        (10, 'TRT10'),
        (11, 'TRT11'),
        (12, 'TRT12'),
        (13, 'TRT13'),
        (14, 'TRT14'),
        (15, 'TRT15'),
        (16, 'TRT16'),
        (17, 'TRT17'),
        (18, 'TRT18'),
        (19, 'TRT19'),
        (20,' TRT20'),
        (21, 'TRT21'),
        (22, 'TRT22'),
        (23, 'TRT23'),
        (24, 'TRT24'),
        (25, 'TST'),
)

#==========VARAS TRABALHISTAS =============================================
VT01AR = '1ª Vara do Trabalho de Angra dos Reis'
VT01ARA = '1ª Vara do Trabalho de Araruama'

VARA_1_SP  = '1a Vara do Trabalho de São Paulo'
VARA_2_SP  = '2a Vara do Trabalho de São Paulo'
VARA_3_SP  = '3a Vara do Trabalho de São Paulo'
VARA_4_SP  = '4a Vara do Trabalho de São Paulo'
VARA_5_SP  = '5a Vara do Trabalho de São Paulo'
VARA_6_SP  = '6a Vara do Trabalho de São Paulo'
VARA_7_SP  = '7a Vara do Trabalho de São Paulo'
VARA_8_SP  = '8a Vara do Trabalho de São Paulo'
VARA_9_SP  = '9a Vara do Trabalho de São Paulo'
VARA_10_SP = '10a Vara do Trabalho de São Paulo'
VARA_11_SP = '11a Vara do Trabalho de São Paulo'
VARA_12_SP = '12a Vara do Trabalho de São Paulo'
VARA_13_SP = '13a Vara do Trabalho de São Paulo'
VARA_14_SP = '14a Vara do Trabalho de São Paulo'
VARA_15_SP = '15a Vara do Trabalho de São Paulo'
VARA_16_SP = '16a Vara do Trabalho de São Paulo'
VARA_17_SP = '17a Vara do Trabalho de São Paulo'
VARA_18_SP = '18a Vara do Trabalho de São Paulo'
VARA_19_SP = '19a Vara do Trabalho de São Paulo'
VARA_20_SP = '20a Vara do Trabalho de São Paulo'
VARA_21_SP = '21a Vara do Trabalho de São Paulo'
VARA_22_SP = '22a Vara do Trabalho de São Paulo'
VARA_23_SP = '23a Vara do Trabalho de São Paulo'
VARA_24_SP = '24a Vara do Trabalho de São Paulo'
VARA_25_SP = '25a Vara do Trabalho de São Paulo'
VARA_26_SP = '26a Vara do Trabalho de São Paulo'
VARA_27_SP = '27a Vara do Trabalho de São Paulo'
VARA_28_SP = '28a Vara do Trabalho de São Paulo'
VARA_29_SP = '29a Vara do Trabalho de São Paulo'
VARA_30_SP = '30a Vara do Trabalho de São Paulo'
VARA_31_SP = '31a Vara do Trabalho de São Paulo'
VARA_32_SP = '32a Vara do Trabalho de São Paulo'
VARA_33_SP = '33a Vara do Trabalho de São Paulo'
VARA_34_SP = '34a Vara do Trabalho de São Paulo'
VARA_35_SP = '35a Vara do Trabalho de São Paulo'
VARA_36_SP = '36a Vara do Trabalho de São Paulo'
VARA_37_SP = '37a Vara do Trabalho de São Paulo'
VARA_38_SP = '38a Vara do Trabalho de São Paulo'
VARA_39_SP = '39a Vara do Trabalho de São Paulo'
VARA_40_SP = '40a Vara do Trabalho de São Paulo'
VARA_41_SP = '41a Vara do Trabalho de São Paulo'
VARA_42_SP = '42a Vara do Trabalho de São Paulo'
VARA_43_SP = '43a Vara do Trabalho de São Paulo'
VARA_44_SP = '44a Vara do Trabalho de São Paulo'
VARA_45_SP = '45a Vara do Trabalho de São Paulo'
VARA_46_SP = '46a Vara do Trabalho de São Paulo'
VARA_47_SP = '47a Vara do Trabalho de São Paulo'
VARA_48_SP = '48a Vara do Trabalho de São Paulo'
VARA_49_SP = '49a Vara do Trabalho de São Paulo'
VARA_50_SP = '50a Vara do Trabalho de São Paulo'
VARA_51_SP = '51a Vara do Trabalho de São Paulo'
VARA_52_SP = '52a Vara do Trabalho de São Paulo'
VARA_53_SP = '53a Vara do Trabalho de São Paulo'
VARA_54_SP = '54a Vara do Trabalho de São Paulo'
VARA_55_SP = '55a Vara do Trabalho de São Paulo'
VARA_56_SP = '56a Vara do Trabalho de São Paulo'
VARA_57_SP = '57a Vara do Trabalho de São Paulo'
VARA_58_SP = '58a Vara do Trabalho de São Paulo'
VARA_59_SP = '59a Vara do Trabalho de São Paulo'
VARA_60_SP = '60a Vara do Trabalho de São Paulo'
VARA_61_SP = '61a Vara do Trabalho de São Paulo'
VARA_62_SP = '62a Vara do Trabalho de São Paulo'
VARA_63_SP = '63a Vara do Trabalho de São Paulo'
VARA_64_SP = '64a Vara do Trabalho de São Paulo'
VARA_65_SP = '65a Vara do Trabalho de São Paulo'
VARA_66_SP = '66a Vara do Trabalho de São Paulo'
VARA_67_SP = '67a Vara do Trabalho de São Paulo'
VARA_68_SP = '68a Vara do Trabalho de São Paulo'
VARA_69_SP = '69a Vara do Trabalho de São Paulo'
VARA_70_SP = '70a Vara do Trabalho de São Paulo'
VARA_71_SP = '71a Vara do Trabalho de São Paulo'
VARA_72_SP = '72a Vara do Trabalho de São Paulo'
VARA_73_SP = '73a Vara do Trabalho de São Paulo'
VARA_74_SP = '74a Vara do Trabalho de São Paulo'
VARA_75_SP = '75a Vara do Trabalho de São Paulo'
VARA_76_SP = '76a Vara do Trabalho de São Paulo'
VARA_77_SP = '77a Vara do Trabalho de São Paulo'
VARA_78_SP = '78a Vara do Trabalho de São Paulo'
VARA_79_SP = '79a Vara do Trabalho de São Paulo'
VARA_80_SP = '80a Vara do Trabalho de São Paulo'
VARA_81_SP = '81a Vara do Trabalho de São Paulo'
VARA_82_SP = '82a Vara do Trabalho de São Paulo'
VARA_83_SP = '83a Vara do Trabalho de São Paulo'
VARA_84_SP = '84a Vara do Trabalho de São Paulo'
VARA_85_SP = '85a Vara do Trabalho de São Paulo'
VARA_86_SP = '86a Vara do Trabalho de São Paulo'
VARA_87_SP = '87a Vara do Trabalho de São Paulo'
VARA_88_SP = '88a Vara do Trabalho de São Paulo'
VARA_89_SP = '89a Vara do Trabalho de São Paulo'
VARA_90_SP = '90a Vara do Trabalho de São Paulo'
VARA_01_ZL = '1ª Vara do Trabalho da Zona Leste de São Paulo'
VARA_02_ZL = '2ª Vara do Trabalho da Zona Leste de São Paulo'
VARA_03_ZL = '3ª Vara do Trabalho da Zona Leste de São Paulo'
VARA_04_ZL = '4ª Vara do Trabalho da Zona Leste de São Paulo'
VARA_05_ZL = '5ª Vara do Trabalho da Zona Leste de São Paulo'
VARA_06_ZL = '6ª Vara do Trabalho da Zona Leste de São Paulo'
VARA_07_ZL = '7ª Vara do Trabalho da Zona Leste de São Paulo'
VARA_08_ZL = '8ª Vara do Trabalho da Zona Leste de São Paulo'
VARA_09_ZL = '9ª Vara do Trabalho da Zona Leste de São Paulo'
VARA_10_ZL = '10ª Vara do Trabalho da Zona Leste de São Paulo'
VARA_11_ZL = '11ª Vara do Trabalho da Zona Leste de São Paulo'
VARA_12_ZL = '12ª Vara do Trabalho da Zona Leste de São Paulo'
VARA_13_ZL = '13ª Vara do Trabalho da Zona Leste de São Paulo'
VARA_14_ZL = '14ª Vara do Trabalho da Zona Leste de São Paulo'
VARA_01_ZS = '1ª Vara do Trabalho da Zona Sul de São Paulo'
VARA_02_ZS = '2ª Vara do Trabalho da Zona Sul de São Paulo'
VARA_03_ZS = '3ª Vara do Trabalho da Zona Sul de São Paulo'
VARA_04_ZS = '4ª Vara do Trabalho da Zona Sul de São Paulo'
VARA_05_ZS = '5ª Vara do Trabalho da Zona Sul de São Paulo'
VARA_06_ZS = '6ª Vara do Trabalho da Zona Sul de São Paulo'
VARA_07_ZS = '7ª Vara do Trabalho da Zona Sul de São Paulo'
VARA_08_ZS = '8ª Vara do Trabalho da Zona Sul de São Paulo'
VARA_09_ZS = '9ª Vara do Trabalho da Zona Sul de São Paulo'
VARA_10_ZS = '10ª Vara do Trabalho da Zona Sul de São Paulo'
VARA_11_ZS = '11ª Vara do Trabalho da Zona Sul de São Paulo'
VARA_12_ZS = '12ª Vara do Trabalho da Zona Sul de São Paulo'
VARA_13_ZS = '13ª Vara do Trabalho da Zona Sul de São Paulo'
VARA_14_ZS = '14ª Vara do Trabalho da Zona Sul de São Paulo'
VARA_15_ZS = '15ª Vara do Trabalho da Zona Sul de São Paulo'
VARA_16_ZS = '16ª Vara do Trabalho da Zona Sul de São Paulo'
VARA_17_ZS = '17ª Vara do Trabalho da Zona Sul de São Paulo'
VARA_18_ZS = '18ª Vara do Trabalho da Zona Sul de São Paulo'
VARA_19_ZS = '19ª Vara do Trabalho da Zona Sul de São Paulo'
VARA_20_ZS = '20ª Vara do Trabalho da Zona Sul de São Paulo'

VARA_1_MG = '1ª VT DE BELO HORIZONTE'
VARA_2_MG = '2ª VT DE BELO HORIZONTE' 
VARA_3_MG = '3ª VT DE BELO HORIZONTE'
VARA_4_MG = '4ª VT DE BELO HORIZONTE'
VARA_5_MG = '5ª VT DE BELO HORIZONTE'
VARA_6_MG = '6ª VT DE BELO HORIZONTE'
VARA_7_MG = '7ª VT DE BELO HORIZONTE'
VARA_8_MG = '8ª VT DE BELO HORIZONTE'
VARA_9_MG = '9ª VT DE BELO HORIZONTE'
VARA_10_MG = '10ª VT DE BELO HORIZONTE'
VARA_11_MG = '11ª VT DE BELO HORIZONTE'
VARA_12_MG = '12ª VT DE BELO HORIZONTE'
VARA_13_MG = '13ª VT DE BELO HORIZONTE'
VARA_14_MG = '14ª VT DE BELO HORIZONTE' 
VARA_15_MG = '15ª VT DE BELO HORIZONTE'
VARA_16_MG = '16ª VT DE BELO HORIZONTE'
VARA_17_MG = '17ª VT DE BELO HORIZONTE'
VARA_18_MG = '18ª VT DE BELO HORIZONTE'
VARA_19_MG = '19ª VT DE BELO HORIZONTE'
VARA_20_MG = '20ª VT DE BELO HORIZONTE'
VARA_21_MG = '21ª VT DE BELO HORIZONTE'
VARA_22_MG = '22ª VT DE BELO HORIZONTE'
VARA_23_MG = '23ª VT DE BELO HORIZONTE'
VARA_24_MG = '24ª VT DE BELO HORIZONTE'
VARA_25_MG = '25ª VT DE BELO HORIZONTE'
VARA_26_MG = '26ª VT DE BELO HORIZONTE' 
VARA_27_MG = '27ª VT DE BELO HORIZONTE'
VARA_28_MG = '28ª VT DE BELO HORIZONTE'
VARA_29_MG = '29ª VT DE BELO HORIZONTE'
VARA_30_MG = '30ª VT DE BELO HORIZONTE'
VARA_31_MG = '31ª VT DE BELO HORIZONTE'
VARA_32_MG = '32ª VT DE BELO HORIZONTE'
VARA_33_MG = '33ª VT DE BELO HORIZONTE'
VARA_34_MG = '34ª VT DE BELO HORIZONTE'
VARA_35_MG = '35ª VT DE BELO HORIZONTE'
VARA_36_MG = '36ª VT DE BELO HORIZONTE'
VARA_37_MG = '37ª VT DE BELO HORIZONTE'
VARA_38_MG = '38ª VT DE BELO HORIZONTE' 
VARA_39_MG = '39ª VT DE BELO HORIZONTE'
VARA_40_MG = '40ª VT DE BELO HORIZONTE'
VARA_41_MG = '41ª VT DE BELO HORIZONTE'
VARA_42_MG = '42ª VT DE BELO HORIZONTE'
VARA_43_MG = '43ª VT DE BELO HORIZONTE'
VARA_44_MG = '44ª VT DE BELO HORIZONTE'
VARA_45_MG = '45ª VT DE BELO HORIZONTE'
VARA_46_MG = '46ª VT DE BELO HORIZONTE'
VARA_47_MG = '47ª VT DE BELO HORIZONTE'
VARA_48_MG = '48ª VT DE BELO HORIZONTE'



VT = (
        (VARA_1_SP, VARA_1_SP),
        (VARA_2_SP, VARA_2_SP),
        (VARA_3_SP, VARA_3_SP),
        (VARA_4_SP, VARA_4_SP),
        (VARA_5_SP, VARA_5_SP),
        (VARA_6_SP, VARA_6_SP),
        (VARA_7_SP, VARA_7_SP),
        (VARA_8_SP, VARA_8_SP),
        (VARA_9_SP, VARA_9_SP),
        (VARA_10_SP, VARA_10_SP),
        (VARA_11_SP, VARA_11_SP),
        (VARA_12_SP, VARA_12_SP),
        (VARA_13_SP, VARA_13_SP),
        (VARA_14_SP, VARA_14_SP),
        (VARA_15_SP, VARA_15_SP),
        (VARA_16_SP, VARA_16_SP),
        (VARA_17_SP, VARA_17_SP),
        (VARA_18_SP, VARA_18_SP),
        (VARA_19_SP, VARA_19_SP),
        (VARA_20_SP, VARA_20_SP),
        (VARA_21_SP, VARA_21_SP),
        (VARA_22_SP, VARA_22_SP),
        (VARA_23_SP, VARA_23_SP),
        (VARA_24_SP, VARA_24_SP),
        (VARA_25_SP, VARA_25_SP),
        (VARA_26_SP, VARA_26_SP),
        (VARA_27_SP, VARA_27_SP),
        (VARA_28_SP, VARA_28_SP),
        (VARA_29_SP, VARA_29_SP),
        (VARA_30_SP, VARA_30_SP),
        (VARA_31_SP, VARA_31_SP),
        (VARA_32_SP, VARA_32_SP),
        (VARA_33_SP, VARA_33_SP),
        (VARA_34_SP, VARA_34_SP),
        (VARA_35_SP, VARA_35_SP),
        (VARA_36_SP, VARA_36_SP),
        (VARA_37_SP, VARA_37_SP),
        (VARA_38_SP, VARA_38_SP),
        (VARA_39_SP, VARA_39_SP),
        (VARA_40_SP, VARA_40_SP),
        (VARA_41_SP, VARA_41_SP),
        (VARA_42_SP, VARA_42_SP),
        (VARA_43_SP, VARA_43_SP),
        (VARA_44_SP, VARA_44_SP),
        (VARA_45_SP, VARA_45_SP),
        (VARA_46_SP, VARA_46_SP),
        (VARA_47_SP, VARA_47_SP),
        (VARA_48_SP, VARA_48_SP),
        (VARA_49_SP, VARA_49_SP),
        (VARA_50_SP, VARA_50_SP),
        (VARA_51_SP, VARA_51_SP),
        (VARA_52_SP, VARA_52_SP),
        (VARA_53_SP, VARA_53_SP),
        (VARA_54_SP, VARA_54_SP),
        (VARA_55_SP, VARA_55_SP),
        (VARA_56_SP, VARA_56_SP),
        (VARA_57_SP, VARA_57_SP),
        (VARA_58_SP, VARA_58_SP),
        (VARA_59_SP, VARA_59_SP),
        (VARA_60_SP, VARA_60_SP),
        (VARA_61_SP, VARA_61_SP),
        (VARA_62_SP, VARA_62_SP),
        (VARA_63_SP, VARA_63_SP),
        (VARA_64_SP, VARA_64_SP),
        (VARA_65_SP, VARA_65_SP),
        (VARA_66_SP, VARA_66_SP),
        (VARA_67_SP, VARA_67_SP),
        (VARA_68_SP, VARA_68_SP),
        (VARA_69_SP, VARA_69_SP),
        (VARA_70_SP, VARA_70_SP),
        (VARA_71_SP, VARA_71_SP),
        (VARA_72_SP, VARA_72_SP),
        (VARA_73_SP, VARA_73_SP),
        (VARA_74_SP, VARA_74_SP),
        (VARA_75_SP, VARA_75_SP),
        (VARA_76_SP, VARA_76_SP),
        (VARA_77_SP, VARA_77_SP),
        (VARA_78_SP, VARA_78_SP),
        (VARA_79_SP, VARA_79_SP),
        (VARA_80_SP, VARA_80_SP),
        (VARA_81_SP, VARA_81_SP),
        (VARA_82_SP, VARA_82_SP),
        (VARA_83_SP, VARA_83_SP),
        (VARA_84_SP, VARA_84_SP),
        (VARA_85_SP, VARA_85_SP),
        (VARA_86_SP, VARA_86_SP),
        (VARA_87_SP, VARA_87_SP),
        (VARA_88_SP, VARA_88_SP),
        (VARA_89_SP, VARA_89_SP),
        (VARA_90_SP, VARA_90_SP),
        (VARA_01_ZL, VARA_01_ZL),
        (VARA_02_ZL, VARA_02_ZL),
        (VARA_03_ZL, VARA_03_ZL),
        (VARA_04_ZL, VARA_04_ZL),
        (VARA_05_ZL, VARA_05_ZL),
        (VARA_06_ZL, VARA_06_ZL),
        (VARA_07_ZL, VARA_07_ZL),
        (VARA_08_ZL, VARA_08_ZL),
        (VARA_09_ZL, VARA_09_ZL),
        (VARA_10_ZL, VARA_10_ZL),
        (VARA_11_ZL, VARA_11_ZL),
        (VARA_12_ZL, VARA_12_ZL),
        (VARA_13_ZL, VARA_13_ZL),
        (VARA_14_ZL, VARA_14_ZL),
        (VARA_01_ZS, VARA_01_ZS),
        (VARA_02_ZS, VARA_02_ZS),
        (VARA_03_ZS, VARA_03_ZS),
        (VARA_04_ZS, VARA_04_ZS),
        (VARA_05_ZS, VARA_05_ZS),
        (VARA_06_ZS, VARA_06_ZS),
        (VARA_07_ZS, VARA_07_ZS),
        (VARA_08_ZS, VARA_08_ZS),
        (VARA_09_ZS, VARA_09_ZS),
        (VARA_10_ZS, VARA_10_ZS),
        (VARA_11_ZS, VARA_11_ZS),
        (VARA_12_ZS, VARA_12_ZS),
        (VARA_13_ZS, VARA_13_ZS),
        (VARA_14_ZS, VARA_14_ZS),
        (VARA_15_ZS, VARA_15_ZS),
        (VARA_16_ZS, VARA_16_ZS),
        (VARA_17_ZS, VARA_17_ZS),
        (VARA_18_ZS, VARA_18_ZS),
        (VARA_19_ZS, VARA_19_ZS),
        (VARA_20_ZS, VARA_20_ZS),

        (VARA_1_MG, VARA_1_MG),
        (VARA_2_MG, VARA_2_MG),
        (VARA_3_MG, VARA_3_MG),
        (VARA_4_MG, VARA_4_MG),
        (VARA_5_MG, VARA_5_MG),
        (VARA_6_MG, VARA_6_MG),
        (VARA_7_MG,  VARA_7_MG),
        (VARA_8_MG,  VARA_8_MG),
        (VARA_9_MG, VARA_9_MG),
        (VARA_10_MG,  VARA_10_MG),
        (VARA_11_MG, VARA_11_MG),
        (VARA_12_MG, VARA_12_MG),
        (VARA_13_MG, VARA_13_MG),
        (VARA_14_MG, VARA_14_MG),
        (VARA_15_MG, VARA_15_MG),
        (VARA_16_MG, VARA_16_MG),
        (VARA_17_MG, VARA_17_MG),
        (VARA_18_MG, VARA_18_MG),
        (VARA_19_MG, VARA_19_MG),
        (VARA_20_MG, VARA_20_MG),
        (VARA_21_MG, VARA_21_MG),
        (VARA_22_MG, VARA_22_MG),
        (VARA_23_MG, VARA_23_MG),
        (VARA_24_MG, VARA_24_MG),
        (VARA_25_MG, VARA_25_MG),
        (VARA_26_MG, VARA_26_MG),
        (VARA_27_MG, VARA_27_MG),
        (VARA_28_MG, VARA_28_MG),
        (VARA_29_MG, VARA_29_MG),
        (VARA_30_MG, VARA_30_MG),
        (VARA_31_MG, VARA_31_MG),
        (VARA_32_MG, VARA_32_MG),
        (VARA_33_MG, VARA_33_MG),
        (VARA_34_MG, VARA_34_MG),
        (VARA_35_MG, VARA_35_MG),
        (VARA_36_MG, VARA_36_MG),
        (VARA_37_MG, VARA_37_MG),
        (VARA_38_MG, VARA_38_MG),
        (VARA_39_MG, VARA_39_MG),
        (VARA_40_MG, VARA_40_MG),
        (VARA_41_MG, VARA_41_MG),
        (VARA_42_MG, VARA_42_MG),
        (VARA_43_MG, VARA_43_MG),
        (VARA_44_MG, VARA_44_MG),
        (VARA_45_MG, VARA_45_MG),
        (VARA_46_MG, VARA_46_MG),
        (VARA_47_MG, VARA_47_MG),
        (VARA_48_MG, VARA_48_MG),


    )

#====================== FUNCTION'S TUTORIAL DROPDOWN DEPENDENT ================================
def get_sp_string():
    sp_string = [
       VARA_1_SP,
        VARA_2_SP,
        VARA_3_SP,
        VARA_4_SP,
        VARA_5_SP,
        VARA_6_SP,
        VARA_7_SP,
        VARA_8_SP,
        VARA_9_SP,
        VARA_10_SP,
        VARA_11_SP,
        VARA_12_SP,
        VARA_13_SP,
        VARA_14_SP,
        VARA_15_SP,
        VARA_16_SP,
        VARA_17_SP,
        VARA_18_SP,
        VARA_19_SP,
        VARA_20_SP,
        VARA_21_SP,
        VARA_22_SP,
        VARA_23_SP,
        VARA_24_SP,
        VARA_25_SP,
        VARA_26_SP,
        VARA_27_SP,
        VARA_28_SP,
        VARA_29_SP,
        VARA_30_SP,
        VARA_31_SP,
        VARA_32_SP,
        VARA_33_SP,
        VARA_34_SP,
        VARA_35_SP,
        VARA_36_SP,
        VARA_37_SP,
        VARA_38_SP,
        VARA_39_SP,
        VARA_40_SP,
        VARA_41_SP,
        VARA_42_SP,
        VARA_43_SP,
        VARA_44_SP,
        VARA_45_SP,
        VARA_46_SP,
        VARA_47_SP,
        VARA_48_SP,
        VARA_49_SP,
        VARA_50_SP,
        VARA_51_SP,
        VARA_52_SP,
        VARA_53_SP,
        VARA_54_SP,
        VARA_55_SP,
        VARA_56_SP,
        VARA_57_SP,
        VARA_58_SP,
        VARA_59_SP,
        VARA_60_SP,
        VARA_61_SP,
        VARA_62_SP,
        VARA_63_SP,
        VARA_64_SP,
        VARA_65_SP,
        VARA_66_SP,
        VARA_67_SP,
        VARA_68_SP,
        VARA_69_SP,
        VARA_70_SP,
        VARA_71_SP,
        VARA_72_SP,
        VARA_73_SP,
        VARA_74_SP,
        VARA_75_SP,
        VARA_76_SP,
        VARA_77_SP,
        VARA_78_SP,
        VARA_79_SP,
        VARA_80_SP,
        VARA_81_SP,
        VARA_82_SP,
        VARA_83_SP,
        VARA_84_SP,
        VARA_85_SP,
        VARA_86_SP,
        VARA_87_SP,
        VARA_88_SP,
        VARA_89_SP,
        VARA_90_SP,
        VARA_01_ZL,
        VARA_02_ZL,
        VARA_03_ZL,
        VARA_04_ZL,
        VARA_05_ZL,
        VARA_06_ZL,
        VARA_07_ZL,
        VARA_08_ZL,
        VARA_09_ZL,
        VARA_10_ZL,
        VARA_11_ZL,
        VARA_12_ZL,
        VARA_13_ZL,
        VARA_14_ZL,
        VARA_01_ZS,
        VARA_02_ZS,
        VARA_03_ZS,
        VARA_04_ZS,
        VARA_05_ZS,
        VARA_06_ZS,
        VARA_07_ZS,
        VARA_08_ZS,
        VARA_09_ZS,
        VARA_10_ZS,
        VARA_11_ZS,
        VARA_12_ZS,
        VARA_13_ZS,
        VARA_14_ZS,
        VARA_15_ZS,
        VARA_16_ZS,
        VARA_17_ZS,
        VARA_18_ZS,
        VARA_19_ZS,
        VARA_20_ZS, 
        ]
    return sp_string


def get_mg_string():
    mg_string = [

        VARA_1_MG,
        VARA_2_MG,
        VARA_3_MG,
        VARA_4_MG,
        VARA_5_MG,
        VARA_6_MG,
        VARA_7_MG,
        VARA_8_MG,
        VARA_9_MG,
        VARA_10_MG,
        VARA_11_MG,
        VARA_12_MG,
        VARA_13_MG,
        VARA_14_MG,
        VARA_15_MG,
        VARA_16_MG,
        VARA_17_MG,
        VARA_18_MG,
        VARA_19_MG,
        VARA_20_MG,
        VARA_21_MG,
        VARA_22_MG,
        VARA_23_MG,
        VARA_24_MG,
        VARA_25_MG,
        VARA_26_MG,
        VARA_27_MG,
        VARA_28_MG,
        VARA_29_MG,
        VARA_30_MG,
        VARA_31_MG,
        VARA_32_MG,
        VARA_33_MG,
        VARA_34_MG,
        VARA_35_MG,
        VARA_36_MG,
        VARA_37_MG,
        VARA_38_MG, 
        VARA_39_MG,
        VARA_40_MG,
        VARA_41_MG,
        VARA_42_MG,
        VARA_43_MG,
        VARA_44_MG,
        VARA_45_MG,
        VARA_46_MG,
        VARA_47_MG,
        VARA_48_MG,
    ]

    return mg_string

# ==================== TRT 2 =================================================================
VARAS_TRABALHISTAS_SP = [

]
#=================== CADASTRO =================================================================

class Cadastro(models.Model):
    pesquisa = models.CharField(
            max_length=200,
            help_text='Cadastre os termos buscados nas bases de dados',
            validators=[MinLengthValidator(4, "O campo do tribunal deve possuir mais que 4 caracteres.")]
    )
    numero = models.CharField(
            unique = True,
            max_length=40,
            help_text='O número do processo tem, geralmente, no mínimo 25 caracteres.',
            validators=[MinLengthValidator(25, "Preencha corretamente o número do Processo")]
)
    CHOICES = (
    (None, None),
    ("Sim", "Sim"),
    ("Não", "Não")
)
    TIPOS_PROCESSOS = (
        ("Individual", "Individual"),
        ("Coletivo", "Coletivo"),
    )
    tipoProcesso =  models.CharField(max_length = 200, choices = TIPOS_PROCESSOS, null=True)
    instância = models.CharField(max_length = 200, choices = GRAU, null=True)
    tribunal = models.CharField(max_length = 200, choices = TRIBUNAIS_TRABALHISTAS, null=True)
    vara =   models.CharField(max_length = 200, choices = VT, null=True)
    turma =   models.CharField(max_length = 200, blank= True, null=True)
    ESTADOS_CHOICES = (
        ("ACRE", "ACRE"),
        ('ALAGOAS','ALAGOAS'),
        ('AMAPÁ', 'AMAPÁ'),
        ('AMAZONAS', 'AMAZONAS'),
        ('BAHIA', 'BAHIA'),
        ('CEARÁ', 'CEARÁ'),
        ('DISTRITO FEDERAL', 'DISTRITO FEDERAL'),
        ('ESPIRITO SANTO', 'ESPIRITO SANTO'),
        ('GOIÁS', 'GOIÁS'),
        ('MARANHÃO', 'MARANHÃO'),
        ('MATO GROSSO', 'MATO GROSSO'),
        ('MATO GROSSO SUL', 'MATO GROSSO SUL'),
        ('MINAS GERAIS', 'MINAS GERAIS'),
        ('PARÁ', 'PARÁ'),
        ('PARAÍBA', 'PARAÍBA'),
        ('PARANÁ', 'PARANÁ'),
        ('PERNAMBUCO', 'PERNAMBUCO'),
        ('PIAUÍ','PIAUÍ'),
        ('RIO DE JANEIRO', 'RIO DE JANEIRO'),
        ('RIO GRANDE DO NORTE', 'RIO GRANDE DO NORTE'),
        ('RIO GRANDE DO SUL', 'RIO GRANDE DO SUL'),
        ('RONDÔNIA', 'RONDÔNIA'),
        ('RORAIMA', 'RORAIMA'),
        ('SANTA CATARINA', 'SANTA CATARINA'),
        ('SÂO PAULO', 'SÂO PAULO'),
        ('SERGIPE', 'SERGIPE'),
        ('TOCATINS', 'TOCATINS'),
    )

    estado = models.CharField(max_length=300, choices = ESTADOS_CHOICES, null = True)
    poloPassivo = models.ForeignKey('Empresa', on_delete=models.PROTECT)
    valorProcesso = models.DecimalField(max_digits=100, decimal_places=2)
    acordoExtrajudicial =   models.CharField(max_length=300, choices = CHOICES, null=True)
    #acordoExtrajudicial =  models.ForeignKey('Options', on_delete=models.PROTECT, null = True)
    TIPOS_DECISAO = (
        ("Despacho", "Despacho"),
        ("Decisao", "Decisao"),
        ("Sentença", "Sentença"),
        ("Acórdão", "Acórdão"),
    )
    tipoDecisao = models.CharField(max_length=300, choices = TIPOS_DECISAO)
    dataJulgamento = models.DateField(default=timezone.now)
    vinculoEmpregaticio =  models.CharField(max_length=300, choices = CHOICES, null=True)

    #class Document(models.Model):

    docfile = models.FileField(upload_to='juris/arquivo/', null=True, blank=True)
    
    #def __str__(self):
        #return self.docfile


#arquivo = models.FileField(upload_to='juris/arquivos/', null = True)
#arquivo =  upload_arquivo()

    observacao = models.CharField(max_length=300, blank = True)
    site = models.URLField()
    created_at = models.DateField(default=timezone.now)
    updated_at = AutoDateTimeField(default=timezone.now)

    # Shows up in the admin list
    def __str__(self):
        return self.numero
        return self.tipoProcesso
        return self.poloPassivo
        return self.vinculoEmpregaticio
        return self.estado
        return self.valorProcesso

    class Meta:
        ordering = ["-created_at", "-updated_at"]

    #def to_dict_json(self):
        #return {
            #'pk': self.pk,
            #'processo': self.numero,
            #'ação': self.tipoProcesso,
            #'empresa': self.poloPassivo,
            #'tribunal': self.tribunal,
            #'vínculo?': self.vinculoEmpregaticio,
        #}

     