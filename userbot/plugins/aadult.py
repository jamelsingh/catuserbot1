import asyncio
import random
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
from userbot import catub
from . import ALIVE_NAME

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "tacat"
SURID = bot.uid

plugin_category = "fun"

@catub.cat_cmd(pattern="adpoem$", command=("adpoem", plugin_category))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "Adult Poem 🥰...")
    await asyncio.sleep(2)
    x = random.randrange(1, 11)
    if x == 1:

        await event.edit(
            "பெண் என்பவள் ஒவ்வொரு பக்கமும் ரசித்துப் படிக்கும் சிறந்த புத்தகம்.!💔🚶🚶"
        )
    if x == 2:

        await event.edit(
            "உன் எழதுகோலால் கவிதை எழுதஆசைதான் எனக்கும் ...என்ன செய்வது உன் எழதுகோலை காலிடுக்கில் பதுக்கி வைத்துள்ளாயே கள்ளா...🍑"
        )

    if x == 3:

        await event.edit(
            "அழகிய மாங்கனிகள் அணைத்து அழுத்தி..விரைத்த காம்பின் வீணை மீட்டுகிறேன் என்னவளே🥰"
        )

    if x == 4:

        await event.edit(
            "ஆடிய கட்டிலை உடைத்தான். ஆனால் அவளின் மனதை வென்று விட்டான்😂"
        )
   
    if x == 5:
 
       await event.edit(
           "என்னவனின் இரு கரங்களும் என் இடுப்பை அணைக்க கண்மூடி அவன் தழுவலை அனுபவிக்கும் அந்நேரம். நாசிதனில் அவனின் வாசம் - மதுவுக்கும் இல்லை அந்த போதை அவன் அணைப்பே சுகம்🥰"
        )

    if x == 6:
     
       await event.edit(
           "இதழ் விரிந்து, இடை விரித்து கொடையாய் தருகிறாய் காமக் குழிதனை..தொப்புள் குழியை சொன்னேன்😂🥰"
       )

    if x == 7:

       await event.edit(
           "விடைகுடுக்கும் ஆடையின்  சுதந்திரம் விடியும் வரை நீளட்டும் அது வரை நீ என் ஆடையாய் இருந்துவிட்டு போ....!"
       )
    if x == 8:
       await event.edit(
           "கதிரவன் முத்தமிடும் மேனியெல்லாம் காதலிப்பவன் காமத்தால் கறை செய்த பாகங்கள் தானே...!"
       )

    if x == 9:
       await event.edit(
           "முத்தம் மட்டும் போதுமென்று,சொல்லிவிட்டு சத்தமில்லாது,களவாடுகின்றான் என் மொத்தத்தையும்,"
       )

    if x == 10:
       await event.edit(
           "அழகிய மாங்கனிகள் அணைத்து அழுத்தி..விரைத்த காம்பின் வீணை மீட்டுகிறேன் என்னவளே"
       )

    if x ==11:
       await event.edit(
           "கன்னத்தோடு கன்னம் உரசி,என் இதழ் கவ்வ வந்த உன்னை தள்ளிவிட்டு நான் எழுந்த போது, என் முந்தானை நழுவி விழ.என் ஆடை மேகத்தில் மறைந்திருந்த இரட்டை நிலா உன் கண் முன் முழுவதுமாய் காட்சி தர இதழ் கவ்வ வந்த உன் இதழ்கள் இடம் மாறி என் மார்புக் காம்பை கவ்வி சுவைத்தது.😗😗"
       )



@catub.cat_cmd(pattern="ajoke$", command=("ajoke", plugin_category))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "Adult joke 🥰...")
    await asyncio.sleep(2)
    x = random.randrange(1, 9)
    if x == 1:

        await event.edit(
            "பெண் என்பவள் ஒவ்வொரு பக்கமும் ரசித்துப் படிக்கும் சிறந்த புத்தகம்.!💔🚶🚶"
        )

    if x == 2:
       await event.edit(
           "தமன்னாக்கு உடம்பு புள்ளா பால் கலர் ஆனா பால் பாக்கெட்தான் ரொம்ப சின்னது 😳"
        )
    if x == 3:
       await event.edit(
           "இரவு வந்தவுடன் ஓழு, உனக்கு எனர்ஜி கொடுக்கும் என் பூலு,விடியும் வரை விளையாட்டு,விரித்து கொள்ளடீ பாப்பா..."
        )

    if x == 4:
       await event.edit(
           "விளக்கை அணைத்துவிட்டு வெட்கத்தை எரிய விட்டால்கரண்டு பில்லுக்குபதிலா ஸ்கூல் பீஸ் கட்ட வேண்டிவரும்"
        )
    if x == 5:
       await event.edit(
           "ஷகிலாவை என் கண்ணில் வைக்கவில்லைஎன் நெஞ்சில் வைத்திருக்கிறேன்அவளோ...என் நெஞ்சில் இருந்து கொண்டுஎன் குஞ்சை எழுப்பு கிறாள்."
        )

    if x == 6:
       await event.edit(
           "என்னடி சொல்றே, இத்தனை நாளா உன் கணவர் செயற்கை உறுப்பை வச்சி ஏமாத்தினதைக் கண்டு பிடிச்சிட்டேன்னு சொல்றே அவர் கிட்டே இதைப் பத்தி ஒரு வார்த்தை கூடக் கேக்கல்லைங்கிறியே, நாக்கைப் பிடுங்கிக்கிற மாதிரி நாலு கேள்வி கேக்கலாமில்ல?”“கேக்கலாம்தான், அதுக்கு அவர் கேட்கிற கேள்விக்கு நான் எதைப் பிடுங்கிக்கிறது?“அவர் என்ன கேக்க முடியும்?”“குழந்தைகள் எல்லாம் எப்படிப் பிறந்ததுன்னு”"
        )

    if x == 7:
       await event.edit(
           ".வெங்கடேஷுக்கு பக்கத்து வீட்டு ஆன்டியுடன் தொடர்பு ஏற்பட்டு விட்டது. இவன் அவள் மார்பகத்தை சுவைத்துகொண்டிருந்தபோது அவள் கணவன்வந்து விட்டான். இவன் " அந்த இடத்துல பாம்பு கடிச்சுருச்சு அங்கிள் அதான் விஷத்தை உறிஞ்சு எடுத்துக்கிட்டிருந்தேன் என்றான். அவரும் சரி சரி என்று அனுப்பி விட்டார். மறு நாள் வெங்கடேஷ் வீட்டு முன் ஆண்களின் நீண்ட க்யூ. அவனவன் கையில் பிடித்துக்கொண்டு நிற்கவெங்கடேஷ் என்னப்பா ஆச்சு என்ன இது அசிங்கமா என்றான். அவர்கள் ஒரே குரலில் சொன்னார்கள் " எங்களையும் பாம்பு கடிச்சுருச்சு.😳😳??"
        )

    if x == 8:
       await event.edit(
            "ராஜி: மாலாக்கா, எங்க வீட்டுக்காரர் ஊருக்குப் போயிருக்காருக்கா. வர நாலு நாள் ஆகும். மாலா: அப்படியா ராஜி! ராஜி: அவர் வர்ற வரைக்கும் துணைக்கு ராத்திரிக்கு என்னோட வந்து படுங்கக்கா. தனியா படுக்க பயமாயிருக்கு. மாலா: சரியாப் போச்சு. உனக்கும், உன் புருஷனுக்கும் இதே வேலைதான். நீ ஊருக்குப் போனாலும் சரி, அவர் என்ன தான் துணைக்கு குப்டுவர்"
        )

    if x == 9:
       await event.edit(
           "Ennaathaan Pombula police irunthaalum. Avanga first night la Husband ta Lathi la adi vaangi Thaan Aaganum."
        )

