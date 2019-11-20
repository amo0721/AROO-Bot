import discord, asyncio, os, sys, setting, datetime

app = discord.Client()
Setting = setting.Settings()
afk = []

@app.event
async def on_ready():
    print("AROO Bot login" % ())
    
@app.event
async def on_member_join(member):
    embed = discord.Embed(title="ㅎㅇㅎㅇ 내 채널 ", description = None, color=0x0000ff)
    embed.add_field(name="닉넴 : " + (member.name), value="아이디 : " + (member.id))
    await app.send_message(app.get_channel(Setting.welcome_channel), embed=embed)

@app.event
async def on_member_remove(member):
    embed = discord.Embed(title="ㅃㅃ", color=0x00ff00)
    embed.add_field(name="닉넴 : " + (member.name), value="아이디 : " + (member.id))
    await app.send_message(app.get_channel(Setting.welcome_channel), embed=embed)

@app.event
async def on_message(message):
    
                id = message.author.id
    
                if message.author.id == Setting.bot_id:
                               return None
                
                if id in afk:
                    embed = discord.Embed(title="잠수 해제됨 ㅅㄱ ", description=str(message.author.name) + "가 해제됨ㅋㅋ", color=0x0000ff)
                    await app.send_message(message.channel, embed=embed)
                    afk.remove(id)
        
    
    
                if message.content.startswith('-게임'):
                    if message.author.server_permissions.administrator:
                        learn = message.content.replace('-게임', "")
                        await app.change_presence(game=discord.Game(name=learn))
                        await app.send_message(message.channel, "게임 바꾸긴 바꿈 근데 노잼일듯")

                if message.content.startswith("-온라인"):
                    embed=discord.Embed(title="AROO Bot 온라인인가 아닌가 그것이 알고싶다", description=None, color=0x00ff00)
                    embed.add_field(name="I'm online!", value="나 아직 살아있음")
                    embed.add_field(name="요청자", value="<@" + str(message.author.name) + ">")
                    await app.send_message(message.channel, embed=embed)  
                
                if message.content.startswith("-초대"):
                    await app.send_message(message.channel, str(message.author.name)+"응 초대 안됨 ㅅㄱㅂ")

                if message.content.startswith("-상태"):
                    if message.author.id == Setting.owner_id:
                        embed = discord.Embed(title="AROO Bot 서버 상태", color=0x00ff00)
                        embed.add_field(name="Owner id", value=Setting.owner_id, inline=True)
                        embed.add_field(name="classic log channel id", value=Setting.err_loging_channel, inline=True)
                        embed.add_field(name="Bot Notice Channel", value=Setting.notice_channel, inline=True)
                        embed.add_field(name="Welcome Channel", value=Setting.welcome_channel, inline=True)
                        embed.add_field(name="Ban User id", value=Setting.ban_user_id, inline=True)
                        await app.send_message(message.channel, embed=embed)
               
                if message.content.startswith('-도움말'):
                    a = datetime.datetime.today().year
                    b = datetime.datetime.today().month
                    c = datetime.datetime.today().day
                    d = datetime.datetime.today().hour
                    e = datetime.datetime.today().minute
                    f = datetime.datetime.today().second
                    embed=discord.Embed(title='`AROO Bot 도움말 목록`', description=None, color=0xb2ebf4)
                    embed.add_field(name='`-온라인`', value='봇이 온라인인지 확인할 수 있음.(실험 아니지?)', inline=False)
                    embed.add_field(name='`-도움말`', value='AROO Bot 도움말을 출력함.', inline=False)
                    embed.add_field(name='`-초대`', value='AROO Bot 개발용이라 초대 ㄴㄴ', inline=False)
                    embed.add_field(name='`-패치노트`', value="봇의 머리를 개조한 거 내용임", inline=False)
                    embed.add_field(name='`-서버정보`', value="서버 정보를 출력함.", inline=False)
                    embed.add_field(name='`-잠수 [사유]`', value="잠수함. 사유도 넣을 수 있음.", inline=False)
                    embed.add_field(name='`-관리자 소개`', value="OverWatch discord Server | 서버 관리자들을 소개하기 싫지만 소개!!!")
                    embed.set_footer(text="관리자 명령어는 '-관리자 도움말' 입력! | " + str(a) + "년 " + str(b) + "월 " + str(c) + "일 " + str(d) + "시 " + str(e) + "분 " + str(f) + "초")
                    await app.send_message(message.channel, embed=embed)

                if message.content.startswith('-관리자 도움말'):
                    embed=discord.Embed(title='`AROO Bot 관리자 도움말 목록`', color=0x00ff00)
                    embed.add_field(name='-공지 [내용]', value="공지 채널에 내용을 공지로 전송함.")
                    embed.add_field(name='-종료', value='봇을 시공의 폭풍으로 날려버림.')
                    embed.add_field(name='-게임 [게임내용]', value='내가 하는 겜 강제로 바꿈. 마크 꿀잼!!!')
                    embed.add_field(name='-상태', value='Setting.py 및 서버 상태를 알려줌.')
                    await app.send_message(message.channel, embed=embed)

                if message.content.startswith("-서버정보"):
                    embed = discord.Embed(title="\"%s\" 서버정보!" % (message.server.name), description=None, color=0X00ff00)
                    embed.add_field(name="서버 소유자", value="<@%s>" % message.server.owner.id, inline=False)
                    embed.add_field(name="서버 생성일", value="%s (UTC)" % (message.server.created_at), inline=False)
                    embed.add_field(name="서버 보안등급", value=message.server.verification_level, inline=False)
                    embed.add_field(name="서버 위치", value=message.server.region, inline=False)
                    embed.add_field(name="서버 잠수채널", value="%s (%s분 이상 잠수이면 이동됨)" % (message.server.afk_channel, message.server.afk_timeout/60), inline=False)
                    embed.set_thumbnail(url=message.server.icon_url)
                    await app.send_message(message.channel, embed=embed)

                if message.content.startswith('-종료'):
                    embed = discord.Embed(title="안녕!!! 나는 시공의 폭풍으로 간다잉~", color=0xff0000)
                    embed.add_field(name="The main module is change to offline.", value="요청자 : " + str(message.author.name))
                    await app.send_message(app.get_channel(Setting.err_loging_channel), embed=embed)
                    quit()

                if message.content.startswith('-관리자 소개'):
                    embed = discord.Embed(title="OverWatch discord의 관리자들을 소개하겠음!", color=0xff0000)
                    embed.add_field(name="아루의 즐거운게임 천국", value="서버 주인(Server Owner)")
                    embed.add_field(name="Jenon", value="서버 관리자/봇 관리자(Server Adminstor/Bot manager)")
                    embed.set_footer(text="Project Bot : Jenon Bot")
                    await app.send_message(message.channel, embed=embed)

    
                if message.content.startswith("-공지"):
                    learn = message.content.replace('-공지', "")
                    if message.author.server_permissions.administrator:
                        a = datetime.datetime.today().year
                        b = datetime.datetime.today().month
                        c = datetime.datetime.today().day
                        d = datetime.datetime.today().hour
                        e = datetime.datetime.today().minute
                        f = datetime.datetime.today().second
                        g = message.author.name
                        embed = discord.Embed(title=str(g) + "의 공지", color=0x00ff00)
                        embed.add_field(name=learn, value="관리자 권한 : 인증✅")
                        embed.set_footer(text=str(a) + "년 " + str(b) + "월 " + str(c) + "일 " + str(d) + "시 " + str(e) + "분 " + str(f) + "초 | 발신자 : " + str(message.author.name))
                        await app.send_message(app.get_channel(Setting.notice_channel), embed=embed)
                        await app.send_message(message.channel, "완료!")
  
                if message.content.startswith('-잠수'):
                    learn = message.content.replace('/잠수', "")
                    a = datetime.datetime.today().year
                    b = datetime.datetime.today().month
                    c = datetime.datetime.today().day
                    d = datetime.datetime.today().hour
                    e = datetime.datetime.today().minute
                    afk.append(id)
                    if learn == '':
                        embed = discord.Embed(title="잠수 시작!", color=0x00ff00)
                        embed.add_field(name=(message.author.name) + "님의 잠수 시작됨 ㅃㅃ!!!", value="잠수 시작 시간 : " + str(a) + "년 " + str(b) + "월 " + str(c) + "일 " + str(d) + "시 " + str(e) + "분")
                        await app.send_message(message.channel, embed=embed)
                    else:
                        embed = discord.Embed(title="잠수 시작!", color=0x00ff00)
                        embed.add_field(name=(message.author.name) + "님의 잠수 시작됨 ㅃㅃ!!!", value="잠수 시작 시간 : " + str(a) + "년 " + str(b) + "월 " + str(c) + "일 " + str(d) + "시 " + str(e) + "분")
                        embed.add_field(name="사유", value=learn)
                        await app.send_message(message.channel, embed=embed)
                        
                if message.content.startswith('-패치노트'):
                    embed = discord.Embed(title="업데이트 내역", color=0x00ff00)
                    embed.add_field(name="●말투 설정 및 봇 신설", value="처음 아루 봇을 만듬/봇의 컨셉에 맞게 말투를 조정함.")
                    embed.add_field(name="●긴급수정:서버 안정화 작업", value="20191120 Update")
                    await app.send_message(message.channel, embed=embed)

                if "-" in message.content:
                    a = datetime.datetime.today().year
                    b = datetime.datetime.today().month
                    c = datetime.datetime.today().day
                    d = datetime.datetime.today().hour
                    e = datetime.datetime.today().minute
                    f = datetime.datetime.today().second
                    embed=discord.Embed(title="AROO Bot Command log", description=str(message.author.name), color=0x0000ff)
                    embed.add_field(name="메세지 내용", value=(message.content))
                    embed.add_field(name="메세지 채널", value="<#" + str(message.channel.id) + ">")
                    embed.set_footer(text=str(a) + "년 " + str(b) + "월 " + str(c) + "일 " + str(d) + "시 " + str(e) + "분 " + str(f) + "초에 발신됨.")
                    await app.send_message(app.get_channel(Setting.err_loging_channel), embed=embed)
                    print("AROO Bot Command Use Log\n발신자:" + str(message.author.name) + "\n발신 서버 : " + str(message.server.name) + "\n내용 : " + str(message.content) % ())

access_token = os.environ["BOT_TOKEN"]
app.run(access_token)
