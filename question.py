import discord
import os

client = discord.Client()  # 接続に使用するオブジェクト
token = os.environ['TOKEN_OF_YOUR_BOT']


# 起動時
@client.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


# メッセージを監視
@client.event
async def on_message(message):
    if message.channel.id == 861529320383578112: #チャンネル限定
        if not message.author.bot: #ボット以外
            #code

        # id=0なら質問者にエラー報告DM
        # idが0以外なら匿名質問する
        if target_channel_id == 0:
            dm = await message.author.create_dm()  # 質問者へDM作成
            await dm.send(
                'Sorry, メッセージを送信できませんでした．'
                'もう1度試してみてください．\n'
                '【質問文】' + question)
        else:
            # 匿名質問させたいチャンネル
            target_channel = client.get_channel(target_channel_id)
            # チャンネルに質問メッセージ送信
            await target_channel.send(question)

# botとしてDiscordに接続(botのトークンを指定)
client.run(token)
