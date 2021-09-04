import discord
from discord.ext import commands
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import datetime
from bs4 import BeautifulSoup
import os



Ids_inner = {
'Title': 'title',
'1730025': '1',
'1419716': '1',
'1424735': '1',
'1762943': '1',
'1669352': '1',
'1391778': '1',
'1748884': '1',
'1729469': '1',
'1652852': '1',
'1665279': '1',
'1325734': '1',
'1457116': '1',
'1576977': '1',
'1419516': '1',
'1730370': '1',
'1722387': '1',
'1211881': '1',
'1589473': '5',
}

#funciones
def Lista_Ids(tags):
    #recibe los tags normales
    Ids = []
    for i, tag in enumerate(tags):
        try:
            Ids.append(tag.td.text)
        except:
            Ids.append("Title")
    return Ids
def pago (tags):
    #recibe tags[numero]
    pago = (tags.text).split('cents')[0][-3:-1]
    if not pago.isdigit():
        pago = pago[-1]
    tareas = (tags.text).split('cents')[1]
    return pago, tareas

def linke(tags):
    try:    
        link = "https://account.appen.com/channels/feca/"+(str(tags.a).split('<a class="a-primary" href="')[1].split('" target="_blank" title="')[0])
    except:
        link = "https://account.appen.com/channels/feca/"+(str(tags.a).split('<a class="a-primary ellipsized" href="')[1].split('" target="_blank" title="')[0])
    return link  
        

def nombre (tags):
    #recibe tags[numero]
    return tags.a.text
def niv(tags):
    try: 
        level = str(tags.i).split('<i class="level-badge level-badge-')[1].split('" i')[0]
    except:
        level = str(tags.i).split('<i class="rating rating-2-')[1].split('"></i>')[0]
    return level


bot = commands.Bot(command_prefix='@bot ', description="Soy wilbot")           


@bot.event
async def on_ready():
    print("Soy Wilbot, estoy conectado....")

@bot.command()
async def iniciar(ctx):
    while True:
        try: 
            options =  webdriver.ChromeOptions()
            options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
            options.add_argument('--headless')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--no-sandbox')
            driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=options)
            time.sleep(3)
            print("conectando")
            driver.get('https://annotate.appen.com/login')


            WebDriverWait(driver, 5)\
            .until(EC.element_to_be_clickable((By.CSS_SELECTOR,

              'input.c-TextInput c-FormField__field c-TextInput--xlarge'.replace(' ', '.'))))\
            .send_keys('caradepapalunes00001-30@yahoo.com')


            WebDriverWait(driver, 5)\
            .until(EC.element_to_be_clickable((By.XPATH,
              '/html/body/div/div[1]/section[2]/div/form/label[2]/div/input')))\
            .send_keys('Ale784596123*')

            WebDriverWait(driver, 5)\
            .until(EC.element_to_be_clickable((By.CSS_SELECTOR,

              'a.b-Button b-Login__submit-button b-Button--medium b-Button--primary'.replace(' ', '.'))))\
            .click()

            print("ingresando")
            time.sleep(10)
            Contador= 0
            while True: 
                try:            
                    driver.get("https://annotate.appen.com/")
                    time.sleep(25)
                    driver.switch_to.frame(driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div/iframe"))
                    driver.find_element_by_css_selector("table.task-listing table table-striped dataTable no-footer".replace(' ', '.'))
                    iframe_source = driver.page_source 
                    page = BeautifulSoup(iframe_source, 'html.parser')
                    tags = page.findAll("tr")
                    A = Lista_Ids(tags)
                    print("Todo encontrado")                                                  
                    for ids in A:
                        if not ids in Ids_inner:
                            pos = A.index(ids)
                            link = linke(tags[pos])
                            pay, tasks = pago(tags[pos])
                            name = nombre(tags[pos])
                            try:
                                Level = niv(tags[pos])
                            except:
                                Level = "0"                                
                            Ids_inner[ids] = tasks 

                            if Level == '1':
                                embed = discord.Embed(title="Appen task(Click para obtener link)", description=name, timestamp=datetime.datetime.utcnow(), color=discord.Color.blue(), url= link)
                                embed.set_thumbnail(url="https://account.appen.com/assets/l-lvl-1-334670863fc97f5e792b3afca6d7b1659bd799243a911d4d85c1694ac1a3b76a.png")
                                embed.add_field(name="Pay in cents", value=pay)
                                embed.add_field(name="#", value=tasks, inline = True)
                                embed.add_field(name="ID", value=ids, inline = True)
                                await ctx.send(embed= embed)                                
                                time.sleep(1)

                            if Level == '2':
                                embed = discord.Embed(title="Appen task(Click para obtener link)", description=name, timestamp=datetime.datetime.utcnow(), color=discord.Color.blue(), url= link)
                                embed.set_thumbnail(url="https://account.appen.com/assets/l-lvl-2-7fd1f2632c95ca2d38d4691df73336f025da84f86d8db9a03ccf8d839c2c90c3.png")
                                embed.add_field(name="Pay in cents", value=pay)
                                embed.add_field(name="#", value=tasks, inline = True)
                                embed.add_field(name="ID", value=ids, inline = True)
                                await ctx.send(embed= embed)
                                time.sleep(1)

                            if Level == '3':
                                embed = discord.Embed(title="Appen task(Click para obtener link)", description=name, timestamp=datetime.datetime.utcnow(), color=discord.Color.blue(), url= link)
                                embed.set_thumbnail(url="https://account.appen.com/assets/l-lvl-3-fe8ba02c5854b60417464dfd975843bcb675400c5f7ee404554859a83c4b3b34.png")
                                embed.add_field(name="Pay in cents", value=pay)
                                embed.add_field(name="#", value=tasks, inline = True)
                                embed.add_field(name="ID", value=ids, inline = True)
                                await ctx.send(embed= embed)
                                time.sleep(1)

                            if Level == '5' or Level== '0':
                                embed = discord.Embed(title="Appen task(Click para obtener link)", description=name, timestamp=datetime.datetime.utcnow(), color=discord.Color.blue(), url= link)
                                embed.add_field(name="Pay in cents", value=pay)
                                embed.add_field(name="#", value=tasks, inline = True)
                                embed.add_field(name="ID", value=ids, inline = True)
                                embed.add_field(name="Level", value="0", inline = True)
                                await ctx.send(embed= embed)
                                time.sleep(1)
                        if ids in A and ids in Ids_inner and ids != "Title":
                            pos = A.index(ids)
                            link = linke(tags[pos])
                            pay, tasks = pago(tags[pos])
                            name = nombre(tags[pos])
                            try:
                                Level = niv(tags[pos])
                            except:
                                Level ="0"
                            if not Ids_inner[ids] == tasks and  Ids_inner[ids]> tasks and tasks<"2" and tasks >="20": #bajando
                                Ids_inner[ids] = tasks
                                if Level == '1':
                                    embed = discord.Embed(title="Appen task(Click para obtener link)-bajando", description=name, timestamp=datetime.datetime.utcnow(), color=discord.Color.blue(), url= link)
                                    embed.set_thumbnail(url="https://account.appen.com/assets/l-lvl-1-334670863fc97f5e792b3afca6d7b1659bd799243a911d4d85c1694ac1a3b76a.png")
                                    embed.add_field(name="Pay in cents", value=pay)
                                    embed.add_field(name="#", value=tasks, inline = True)
                                    embed.add_field(name="ID", value=ids, inline = True)
                                    await ctx.send(embed= embed)                                
                                    time.sleep(1)

                                if Level == '2':
                                    embed = discord.Embed(title="Appen task(Click para obtener link)-bajando", description=name, timestamp=datetime.datetime.utcnow(), color=discord.Color.blue(), url= link)
                                    embed.set_thumbnail(url="https://account.appen.com/assets/l-lvl-2-7fd1f2632c95ca2d38d4691df73336f025da84f86d8db9a03ccf8d839c2c90c3.png")
                                    embed.add_field(name="Pay in cents", value=pay)
                                    embed.add_field(name="#", value=tasks, inline = True)
                                    embed.add_field(name="ID", value=ids, inline = True)
                                    await ctx.send(embed= embed)
                                    time.sleep(1)

                                if Level == '3':
                                    embed = discord.Embed(title="Appen task(Click para obtener link)-bajando", description=name, timestamp=datetime.datetime.utcnow(), color=discord.Color.blue(), url= link)
                                    embed.set_thumbnail(url="https://account.appen.com/assets/l-lvl-3-fe8ba02c5854b60417464dfd975843bcb675400c5f7ee404554859a83c4b3b34.png")
                                    embed.add_field(name="Pay in cents", value=pay)
                                    embed.add_field(name="#", value=tasks, inline = True)
                                    embed.add_field(name="ID", value=ids, inline = True)
                                    await ctx.send(embed= embed)
                                    time.sleep(1)

                                if Level == '5' or Level== '0':
                                    embed = discord.Embed(title="Appen task(Click para obtener link)-bajando", description=name, timestamp=datetime.datetime.utcnow(), color=discord.Color.blue(), url= link)
                                    embed.add_field(name="Pay in cents", value=pay)
                                    embed.add_field(name="#", value=tasks, inline = True)
                                    embed.add_field(name="ID", value=ids, inline = True)
                                    embed.add_field(name="Level", value="0", inline = True)
                                    await ctx.send(embed= embed)
                                    time.sleep(1)

                            if not Ids_inner[ids] == tasks and  Ids_inner[ids]< tasks and tasks<"2" and tasks >="20":#subiendo
                                Ids_inner[ids] = tasks
                                if Level == '1':
                                    embed = discord.Embed(title="Appen task(Click para obtener link)-subiendo", description=name, timestamp=datetime.datetime.utcnow(), color=discord.Color.blue(), url= link)
                                    embed.set_thumbnail(url="https://account.appen.com/assets/l-lvl-1-334670863fc97f5e792b3afca6d7b1659bd799243a911d4d85c1694ac1a3b76a.png")
                                    embed.add_field(name="Pay in cents", value=pay)
                                    embed.add_field(name="#", value=tasks, inline = True)
                                    embed.add_field(name="ID", value=ids, inline = True)
                                    await ctx.send(embed= embed)                                
                                    time.sleep(1)

                                if Level == '2':
                                    embed = discord.Embed(title="Appen task(Click para obtener link)-subiendo", description=name, timestamp=datetime.datetime.utcnow(), color=discord.Color.blue(), url= link)
                                    embed.set_thumbnail(url="https://account.appen.com/assets/l-lvl-2-7fd1f2632c95ca2d38d4691df73336f025da84f86d8db9a03ccf8d839c2c90c3.png")
                                    embed.add_field(name="Pay in cents", value=pay)
                                    embed.add_field(name="#", value=tasks, inline = True)
                                    embed.add_field(name="ID", value=ids, inline = True)
                                    await ctx.send(embed= embed)
                                    time.sleep(1)

                                if Level == '3':
                                    embed = discord.Embed(title="Appen task(Click para obtener link)-subiendo", description=name, timestamp=datetime.datetime.utcnow(), color=discord.Color.blue(), url= link)
                                    embed.set_thumbnail(url="https://account.appen.com/assets/l-lvl-3-fe8ba02c5854b60417464dfd975843bcb675400c5f7ee404554859a83c4b3b34.png")
                                    embed.add_field(name="Pay in cents", value=pay)
                                    embed.add_field(name="#", value=tasks, inline = True)
                                    embed.add_field(name="ID", value=ids, inline = True)
                                    await ctx.send(embed= embed)
                                    time.sleep(1)

                                if Level == '5' or Level== '0':
                                    embed = discord.Embed(title="Appen task(Click para obtener link)-subiendo", description=name, timestamp=datetime.datetime.utcnow(), color=discord.Color.blue(), url= link)
                                    embed.add_field(name="Pay in cents", value=pay)
                                    embed.add_field(name="#", value=tasks, inline = True)
                                    embed.add_field(name="ID", value=ids, inline = True)
                                    embed.add_field(name="Level", value="0", inline = True)
                                    await ctx.send(embed= embed)
                                    time.sleep(1)                           


                except Exception as e:  
                    print("Ha ocurrido 1 error =>", type(e).__name__)
                    time.sleep(15)
                    Contador = Contador +1

                    if Contador == 3:
                        raise ValueError("Error el navegador esta detenido")
                        break
                

        except Exception as e:
            print("Ha ocurrido 2 error =>", type(e).__name__)            

bot.run("Nzg4NTIxMjM4NTIyNzU3MTIx.X9ktoQ.F7SQXu4shpoK0L3hyn_UquLxiiQ")