import discord
from discord.ext import commands
import random

TOKEN = 'Bot_Token_Here'

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.members = True
intents.message_content = True  # Bu satır Message Content Intent'i açar

bot = commands.Bot(command_prefix="!", intents=intents)

# Şakalar
jokes = [
    "Neden bilgisayarlar hiç gülmez? Çünkü çok ciddi işler yaparlar.",
    "Şu an en zeki hayvan kimdir? Kesinlikle bir 'ağaç'.",
    "Bir inek neden çok iyi şarkıcıdır? Çünkü ses tonları çok derindir.",
    "Rüzgar neden sürekli şişmanlayıp zayıflar? Çünkü her zaman sağa sola savruluyor!",
    "Neden pizzalar iyi futbolcudur? Çünkü her zaman topu sektirirler.",
    "Hayvanat bahçesinde neden bazı hayvanlar çok dikkatli? Çünkü her an bir şeyler hırpalanabilir!",
    "Bir kuş neden uçamaz? Çünkü tüyleri kollarına sıkışmış!",
    "Matematik kitabı neden üzgündü? Çünkü çok problemi vardı.",
    "Neden bilgisayarlar asla tatile gitmez? Çünkü sürekli 'işlem yaparlar.'",
    "Karpuz neden tenis oynayamaz? Çünkü her zaman kesiliyor!",
    "Gözlük neden ağlamaz? Çünkü gözlüğün gözleri yoktur!",
    "Telefonlar neden akıllıdır? Çünkü sürekli çağrılara cevap verirler!",
    "Nasıl bir insan bir kediyle arkadaş olabilir? Kedi her zaman yakalanmaya çalışıyordur!",
    "Eğlenceli bir bilgisayar nedir? 'Macbook Pro' değil tabii ki!",
    "Gitar çalmayı ne zaman öğrenirsin? Akorları birleştirince!",
    "Kafede neden sessiz olmalısınız? Çünkü herkes çayın tadını çıkarmaktadır!",
    "Süt neden yavaşça gelir? Çünkü hayvanların bir araya gelmesi zaman alır!",
    "Neden evdeki eşyalar hiç gülmez? Çünkü her zaman doğru bir iş yaparlar!",
    "Çay neden sinirliydi? Çünkü altı kaynıyordu!",
    "Neden fotokopi makineleri hep üzgündür? Çünkü hep başkalarını kopyalarlar.",
    "Bir inek neden gökyüzüne bakmaz? Çünkü sadece yere bakar!",
    "Hangi hayvan şarkı söyler? Balina!",
    "Bir bilgisayar neden sıcak olabilir? Çünkü işlemcisi çok yoğun çalışıyordur.",
    "Zombi neden pizza sever? Çünkü her zaman 'beyin' istiyordur.",
    "Yılanlar neden kafalarını eğemez? Çünkü onları tıklatıyorlar!",
    "Bir bilgisayar neden her zaman çökme noktasına gelir? Çünkü çok fazla iş yapar!",
    "Karpuz neden tatlıdır? Çünkü suyun içinde kaybolmuş gibidir!",
    "Hayalet neden bilgisayarları sevmez? Çünkü onları izlerken hissediyorlar!",
    "Neden tembel insanlar uzaya gitmez? Çünkü onlar, hiçbir zaman yerçekimine 'bakarlar!'",
    "Bir bilgisayar neden hiç şikayet etmez? Çünkü işlemci hızına göre çalışıyor!",
    "Hangi hayvan en hızlı koşar? Zeytin dalı!",
    "Kediler neden çok iyi yazar? Çünkü her zaman 'noktalama' yaparlar.",
    "Sakız neden çok iyi bir arkadaş? Çünkü her zaman çekilir!",
    "Kuşlar neden futbolu sever? Çünkü çok iyi 'uçucu'lar!",
    "Eğer bir robot boks yaparsa, kimin kazanacağı belli olur: Bir kutu taşar!",
    "Bir bilgisayar neden yazmayı sevmez? Çünkü hep 'bilgi' kaybeder!",
    "Dondurma neden soğuktur? Çünkü tatlılığı bekler!",
    "Çamaşır makinesi neden yanlış hareket eder? Çünkü ona hiç kimse talimat vermez!",
    "Zebra neden bilgisayarları çok sever? Çünkü 'taban'larda daha rahat hissediyor!",
    "Bir pizza neden neşelidir? Çünkü hep sıcak ve taze kalır!",
    "Neden bilgisayarlar çok iyi dinler? Çünkü 'harddisk'leri çok geniştir!",
    "Çamaşır makinesi neden hayatı çok basit tutar? Çünkü ona bulaşıklar bağlıdır!",
    "Ayakkabılar neden sabırlıdır? Çünkü her zaman 'adım' atmaya ihtiyaçları vardır!",
    "Kuşlar neden rahatça şarkı söyler? Çünkü tüyleri 'rüzgar'la büyür!"
]


# Embed mesajları tek bir renkte yapacağız
embed_color = discord.Color.blue()

# !yardım komutu
@bot.command()
async def yardım(ctx):
    embed = discord.Embed(title="Yardım Komutları", color=embed_color)
    embed.add_field(name="!yardım", value="Komutları listelemek için.", inline=False)
    embed.add_field(name="!yasakla [Kullanıcı]", value="Kullanıcıyı sunucudan yasaklar.", inline=False)
    embed.add_field(name="!at [Kullanıcı]", value="Kullanıcıyı sunucudan atar.", inline=False)
    embed.add_field(name="!sustur [Kullanıcı]", value="Kullanıcıyı susturur.", inline=False)
    embed.add_field(name="!sessustur [Kullanıcı]", value="Kullanıcıyı ses kanalında susturur.", inline=False)
    embed.add_field(name="!sessağırlaştır [Kullanıcı]", value="Kullanıcıyı ses kanalında susturur.", inline=False)
    embed.add_field(name="!sil [Sayı]", value="Belirtilen sayıda mesajı siler.", inline=False)
    embed.add_field(name="!şaka", value="Rastgele bir şaka gönderir.", inline=False)
    embed.add_field(name="!konuştur [Kullanıcı] [Mesaj]", value="Kullanıcıyı konuşturur.", inline=False)
    await ctx.send(embed=embed)

# !konuştur komutu (Webhook ile mesaj gönderme)
@bot.command()
async def konuştur(ctx, user: discord.User, *, message):
    # Webhook URL'sini almak için kanalın webhook'larını alalım
    channel = ctx.channel
    webhooks = await channel.webhooks()

    if webhooks:
        webhook = webhooks[0]  # İlk webhook'u alıyoruz
    else:
        # Eğer webhook yoksa, yeni bir webhook oluşturuyoruz
        webhook = await channel.create_webhook(name="Konuştur Webhook")

    # Webhook ile mesaj gönderiyoruz
    await webhook.send(content=message, username=user.name, avatar_url=user.avatar.url)
    
    # DM ile kullanıcıya bildirim gönderelim
    await user.send(f"Şu mesajla konuşturuldun: {message}")
    await ctx.send(f"{user} başarıyla konuşturuldu ve DM gönderildi.", embed=discord.Embed(description=f"**Mesaj:** {message}", color=embed_color))

# !yasakla komutu
@bot.command()
async def yasakla(ctx, user: discord.User, *, reason="Sebep belirtilmedi"):
    await ctx.guild.ban(user, reason=reason)
    embed = discord.Embed(title="Yasaklama İşlemi", description=f"{user} başarıyla yasaklandı.", color=embed_color)
    embed.add_field(name="Sebep", value=reason, inline=False)
    await ctx.send(embed=embed)

# !at komutu
@bot.command()
async def at(ctx, user: discord.User, *, reason="Sebep belirtilmedi"):
    await ctx.guild.kick(user, reason=reason)
    embed = discord.Embed(title="Atılma İşlemi", description=f"{user} başarıyla sunucudan atıldı.", color=embed_color)
    embed.add_field(name="Sebep", value=reason, inline=False)
    await ctx.send(embed=embed)

# !sustur komutu
@bot.command()
async def sustur(ctx, user: discord.User, *, reason="Yok"):
    member = await ctx.guild.fetch_member(user.id)  # User'ı Member'a dönüştürme
    mute_role = discord.utils.get(ctx.guild.roles, name="Muted")
    if not mute_role:
        mute_role = await ctx.guild.create_role(name="Muted")
        for channel in ctx.guild.channels:
            await channel.set_permissions(mute_role, speak=False, send_messages=False)
    await member.add_roles(mute_role, reason=reason)
    embed = discord.Embed(title="Susturma İşlemi", description=f"{user} başarıyla susturuldu! Sebep: {reason}", color=embed_color)
    await ctx.send(embed=embed)

# !sil komutu
@bot.command()
async def sil(ctx, amount: int):
    await ctx.channel.purge(limit=amount)
    embed = discord.Embed(description=f"{amount} mesaj başarıyla silindi.", color=embed_color)
    await ctx.send(embed=embed)

# !şaka komutu
@bot.command()
async def şaka(ctx):
    joke = random.choice(jokes)
    embed = discord.Embed(description=joke, color=embed_color)
    await ctx.send(embed=embed)

# RPC için
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    await bot.change_presence(activity=discord.Game(name="Arouwa.enderman.cloud"))

bot.run(TOKEN)
