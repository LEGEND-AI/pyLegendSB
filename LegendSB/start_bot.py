async def start_bot(Client):
    await Client.start()
    try:
       x = await Client.get_me()
       print(f"SpamBot - [INFO]: @{x.first_name} started ✓")
    except:
       print(f"SpamBot - [INFO]: Client started ✓")
