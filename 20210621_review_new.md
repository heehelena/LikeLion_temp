```python
import os
```


```python
os.getcwd()
```




    'C:\\Users\\myhkj'




```python
from selenium import webdriver
from bs4 import BeautifulSoup
```


```python
driver = webdriver.Chrome('chromedriver_90')
```


```python
url = 'https://www.amazon.com/'
driver.get(url)
```


```python
sel_search = driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')
sel_btn = driver.find_element_by_xpath('//*[@id="nav-search-submit-button"]')

print(sel_search.tag_name, sel_btn.tag_name)
```

    input input
    


```python
sel_search.clear()
sel_search.send_keys("kindle")
sel_btn.click()
```


```python
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")
soup.title
```




    <title>Amazon.com : kindle</title>




```python
url = "https://www.amazon.com/All-new-Kindle-Oasis-now-with-adjustable-warm-light/dp/B07F7TLZF4/ref=sr_1_1?dchild=1&amp;keywords=kindle&amp;qid=1624257040&amp;sr=8-1"
driver.get(url)
```


```python
import time
time.sleep(3)
```

전체 평점 확인


```python
sel_rate = driver.find_element_by_xpath('//*[@id="acrCustomerReviewText"]')
sel_rate.click()
```

전체 리뷰 확인


```python
sel_all_reviews = driver.find_element_by_xpath('//*[@id="reviews-medley-footer"]/div[2]/a')
sel_all_reviews.click()
```


```python
page = driver.page_source
soup = BeautifulSoup(page, 'lxml')
soup.title
```




    <title>Amazon.com: Customer reviews: Kindle Oasis – Now with adjustable warm light – Ad-Supported</title>




```python
all_r = soup.find_all("span", class_='a-size-base review-text review-text-content')
len(all_r)
all_r[0].text.strip()
```




    'This is my 11th Kindle. Their last Oasis model should have been technology forward enough to have a USB-C charging. The lack of this charging port is totally unacceptable. I am angry over this. EVERY cell phone sold is either USB-C or Lightning. Just a quick walk through a Best Buy will show numerous computers with USB-C charging. Going with a Micro USB port is an insult to the target users of this flagship device. The head of the Kindle project and any engineer that advocated for it should be fired.'




```python
all_reviews = []

for one in all_r:
    tmp = one.text
    review = tmp.strip()
    all_reviews.append(review)
    
all_reviews
```




    ['This is my 11th Kindle. Their last Oasis model should have been technology forward enough to have a USB-C charging. The lack of this charging port is totally unacceptable. I am angry over this. EVERY cell phone sold is either USB-C or Lightning. Just a quick walk through a Best Buy will show numerous computers with USB-C charging. Going with a Micro USB port is an insult to the target users of this flagship device. The head of the Kindle project and any engineer that advocated for it should be fired.',
     "Pros:__________•  It’s small, provides basically two simple physical controls, and a sleek premium aluminum design that makes it beautiful to look at without showing off.•  The screens warm temperature display works like a charm. You can either adjust it manually in the setting section or just set it to automatically active with sunrise and sunset. I just put in an automatic timer and overall found it a pleasure to use this feature at night. The warm effect doesn’t bring in any eye irritation to me, at night or day, which a computer screen does.•  Surprisingly for me, I found the need to apply the warm temperature display on all day. The reason why is because the effect creates the illusion of flipping through old pages in a book. I’m always a physical book person, so this feature brings in the comfort of that feeling.  It makes it look like real paper! Still, I only use the cool display when it’s super bright out, but other than that the warm display is perfect regardless of day or night.•  You have many intensity levels of cool brightness to ranges of the warm temperature effect that can match your need. From mild yellow to full-on amber color, Amazon finally put in the right software for this display because I’m getting a clear display and no glare regardless of any ambient lighting.•  The E-ink display is very fast and efficient. I mean you’re just reading so the processing power isn’t that much as I didn’t notice any ghosting while reading.•  This is one of the only times that I’m glad for a bezel border because I can always place my hand at the perfect spot on the device, right underneath the page buttons.•  The page buttons themselves provide great feedback when I press them.  They’re not loud but it does give you that little click, which I love. You can use the touch screen to turn pages, but I felt the buttons provide a better experience.•  Regardless if you're left or right-handed, the device is ambidextrous! I flip the screen to my left the display adapts to it, just as if I flipped it to the right. The experience is the same for all.•  I took it out in a clear sunny day and the anti-glare matte display screen provided perfect viewing angles even when the sun was hitting at it the most.•  The touch screen is responsive as I like that it has a soft-touch texture on it. It creates a pleasurable experience and kills the creations of my fingerprint.•  IPX8 waterproof means it can be washed off and taken almost anywhere. I didn’t submerge it in a pool of water but an IPX8 will stand almost all forms of water issues (just don’t use it under the water.)•  Bluetooth is super-fast. Connecting my Airpods took less than 20 seconds, and the feedback is spot on.•  Battery life is in no way going to be an issue. From my one battery test, I got around 21 hours of use! The average person will probably read 30-40 minutes a day with this.  Having Wi-Fi on will eat a lot more but, in the end, the math doesn’t lie.•  The software of highlighting text, placing bookmarks, getting extra info about your book, and adding notes is very straight forward and doesn’t require digging around the system to use them. For me, one feature I use a lot is tapping a word and get the dictionary pulled up for the word (you need Wi-Fi).•  You can input MOBI, PDF, and TXT files on this device (I’ll go into more details later on).•  One cool feature I like is that if you use your kindle email address, you can upload files to your Oasis. I found this 10x quicker as I used this format when transferring my Steve Jobs autobiography book from my IPad to the Oasis (via email).•  At the time pf my review, I found 10 different fonts, 14 sizes, and numerous alignment choices. I can save numerous themes and have the option to switch back and forth if I wanted to. I found this feature helpful if more than one person uses this device.•  The books themselves are pretty cheap to buy on Amazon. It’s even better if you’re a Prime member because you can “borrow” books from the Prime Reading catalog. There is also Amazon First Reads that I like but overall, if you get this device, Amazon is the way to go in getting your books/magazines.•  Unlike a smartphone, I know that if you treat your Oasis right, you’ll get a pretty good shelve life with it.Cons and Oks:__________•  Micro-USB! Are they serious? Just like Amazon’s previous models, no USB-C connector. Micro-USB brings slow for charging and importing files.  With Micro-USB, I’m getting around 3 hours, 0-100%, for a complete charge. I don't know who decided to have this design feature, but come on!•  No headphone jack! No idea why this isn’t built-in because they even have the room for it on the device.•  Getting used in finding your brightness and temperature setting will take some time. Amazon gives a lot of options on the display, as I spent a decent amount of time just figuring out which type of lighting I wanted.•  The keyboard is a touchscreen keyboard.  So expect a slow typing rate. Sadly I can’t apply the tracing effect that many androids and google phones provide on their keyboards.• The aluminum design does make this slippery to hold, and it’s able to slide off my lap pretty easily.• Also, with aluminum, it takes in the heat or the cold a lot quicker if you leave it outdoors or in a hot car.• Without a decent cover, it feels like I’m holding a piece of metal than the feeling of holding a book.•  Can’t connect to 5GhZ Wi-Fi network.•  Even if this Oasis looks the same as its previous models, I found out that you can’t really use the same covers.  My colleague has the older model and issue we found is that the magnet covers of the last case model don’t stick with the new Oasis.  Almost the same size and weight, you expect that older covers to work, but nope. I’ll have to pay for a new case cover.•  At the time of my review, I get ads on the lock screen of the device. You can remove them, but you have to pay around $20 to make it ad-free. I found this ridiculous given what you’re already paying for it.•  As I mentioned before, you can upload MOBI, PDF, and TXT files on this device.  This is cool, but when I put in a simple pdf file (composed of a small story) the formatting gets lost in the process. The paragraphs were mashed together, there was a delay when you wanted to turn to the next page, and overall it looks like a big mess.  Now, this could be just a one-time event, but I have to assume any third party software that goes into the Oasis will face some issues (Importing audiobooks did work flawlessly though).•  No microSD. That means the storage you have is what you’re going to have forever. This is buzz kill because I know for only 8 GB (Minus 1 GB for the initial software) you’re going to only have maybe 20 audiobooks go have on storage.  It seems more appropriate, given the shelf life of this device, to just invest in the 32 GB since there is no way to upgrade the 8 GB.•  It’s small, but not small enough to fit your pocket. Be careful where you put it because I feel like I can bend this without any issue if I wanted to.•  The browser feature, I believe, is very experimental. Because of the display, many webpages are shown up broken or just unreadable. Obliviously this isn’t for web browsing, but it’s a feature they provide that I just ignore.•  It’s almost the same in software and design as its previous model. With the price, I was expecting Amazon to a least redesign it into something different (maybe less in the bezels).  It’s still a beautiful design but, given the identical looks as its previous model, as the only main difference is the warm color effect. I know this is what Amazon is advertising but they had 2 years to redesign it. I guess the saying goes “if it ain't broke, don't fix it.”Bottom Line:__________As not having a Kindle before this, I would say that I’m having a pleasant time reading with this.  I always prefer a “real” book to read, but having thousands of books at my fingertips, it does reduce that need. To be honest, it’s kind of scary to see the possibility that kids can use this more than a physical book. It reminds me of a scene from the 1960’s film “The Time Machine,” where George goes into to future to find out that all the books he touches turn into a fine powder because no one has used them in centuries.But ignoring that thought, there really isn’t any competition for devices like these, and Amazon does know how to build them. It's sleek, fast, and most importantly, the screen is superb in reading. The warm light effect does make me feel that I’m still reading an old book, while the battery life is holding its ground.Note, if anyone has the previous model of the Oasis, don’t bother buying this.  It’s the same thing, except without the warm display and some small software upgrades. For new people, I recommend that you invest in the 32 GB because 8 GB is not nearly enough (given that you can’t even install a MicroSD to it). There are some smaller issues with the design of the device that make me feel like I’m holding a machine instead of a book (not to mention the Micro-USB!), but for those who want to take a leap in digital reading, this is the way to go.Overall: An above-average device for book readers of all ages, and a small step forward in the extinction of physical books.Hope I was a help to you.Love,Honest Reviewer.",
     'I wrote a lengthy critical review of the 2017 Oasis, which was the first Kindle that I’ve ever returned out of every top model. I mainly criticized the cold and slippery aluminum shell for intruding on, rather than disappearing from, the reading experience. But along with those criticisms, I praised its bigger 7” screen as the one aspect that I would miss. And now, with the upgrade of that screen to one with adjustable color temperature, I decided to give the 2019 Oasis a try, even though its design was unchanged from 2017.Cutting right to the chase: the adjustable color temperature screen is the greatest advance in Kindles since self-illuminating screens were introduced on the first Paperwhite… period, full-stop. And, at least for this reader, there’s no going back after trying it out. It’s that good, and that much of a game changer.With both warmth and brightness (they have separate controls) turned up to about the midway point, reading on a Kindle transitioned for the first time from merely reading words, to the experience of reading words on a paper page in a book. This might sound like “Who cares?” nonsense to most people, but if you’re in that small minority of the public buying a high-end Kindle, you understand what I mean, and it’s that kind of difference that you’re paying for.The new lighting also transforms the experience of reading in a completely dark room. On existing Kindles, I could never find quite the right light level. If it was as bright as I wanted it to be, that felt too harsh on my eyes. But bringing brightness down to a level that felt comfortable seemed too dim. Now, by simply increasing the lighting warmth on the new Oasis, you can have brighter light with no harshness in a dark room, making reading much easier on the eyes.Finally, I’m happy to say that Amazon seems to have (finally!) nailed the quality control issues that have plagued new Kindle lighting systems in the past: No splotches. No dark spots. No shadows. No weird color casts. Just smooth, even, beautiful lighting across the screen.So, is this the perfect Kindle for me? No. The perfect Kindle would be this new 7” screen in a Voyager form factor. The ergonomics of the Oasis are still not great for me, although my satisfaction with the new screen appears to make the annoyances matter less. The 2019 Oasis is not only a keeper for me, but I’m actually trading in both my Voyager and original Oasis.Thanks for taking the time to read my review and I hope you find it helpful in making a buying decision. Time permitting, I do try to answer any questions posted in the comments section.',
     'Your browser does not support HTML5 video.\n\n\n  \xa0I decided to finally upgrade my Kindle from the first Paperwhite when I found out I could get a 25% discount and a $5 Amazon gift card for trading in my very old and unused Kindle Keyboard 1st gen, as well as other bonuses of 6 months free Kindle Unlimited (approx $60) plus a 30 day Audible trial.I’m very happy with it and it has some great features.I do like the adjustable amber tint, but I also really like the ability to invert the colors to white print on a black background.  This is even easier on the eyes, but it does have a noticeable (and irritating) white flash every few page turns when using the buttons, and almost with every page turn when advancing with the touch screen.  I believe this is the e-ink refreshing.  I will probably use the black inverted color only when I’m reading outside in bright sunlight.I also am really happy to have buttons to turn the page again.  It’s the ultimate laziness to be able to just keep your thumb in the button and depress it to turn the page instead of having to actually move your thumb a half inch to touch the screen, but hey, why move a half inch when your can push down 1/16th of an inch?  All that extra movement add up over the years.The real reason I like the buttons is this: I live in Alaska and we have very long, cold nights.  But even in the winter, we turn down the heat at night.  I read in bed every single night, tucked all cozy and warm under my down comforter... except for having to have my hand out in order to touch the screen on my Paperwhite to turn the page.  My hand starts to get very cold.  It’s uncomfortable.  My half frozen hand takes away from my happy bedtime reading experience.  With the Oasis, I can keep my hand under the blankets and just push the button.  You don’t know what a big deal this is until you spend night after night with a frozen hand.I also like that you can select which button to the the page advance button and which is the page back button.  The Oasis comes set up with the top button as the page advance and the bottom as the page back, but I switched them: the bottom is the advance, the top is the back.  I hold my ereaders at the bottom sides, and had to stretch my thumb to advance the page when it was set for the top button.  It’s just easier and more comfortable to use the bottom button.  And this is cool: the bottom button stays as my page advance button even when I rotate the Oasis 180 to use left handed!!  Smart!!Others have covered the size and weight so I won’t go it I all that except to say it’s comfortable to hold.  I do use the official Amazon Premium leather cover and it fits perfectly, and the magnetic closure/sleep/wake functions work perfectly also.Dislike:  Nothing with the ereader itself, but with however Amazon picks the “special offers”.  From what I read, these offers are supposed to be tailored off of a person’s reading history/preferences.  I may be wrong.The books they are featuring for me are “romance” genre.  I am sooo not a romance genre girl.  I don’t believe I’ve ever purchased this genre in my life. I’m a hardcore sci-fi/dystopian. I have an adverse reaction when I see romance special offer.Other than that, some of the complaints by others leaves me wondering.I just don’t think it’s THAT big of deal that it has a micro usb.  Really, it’s just not that hard to figure out the big end of the cable from the small end.  As for charging speed, charge mine while I’m sleeping at night so it doesn’t matter if it takes 1 hour or 4. I suppose having to carry a micro usb cord and charger  when other devices use a usb-c cord/charger may be annoying but I think I can find 2 square inches in my purse/pocket/bag/backpack for it.Also remember that this is an e-reader.  It’s not a tablet, computer or smartphone, nor does it make any claims to be.  Expecting an ereader to function basically like a computer/tablet/smartphone is expecting too much.  It does an outstanding job at doing it’s job as an ereader.I have sent many different type of files to my Paperwhite using my kindle email address and it’s worked excellent with that old ereader, so I expect this new Oasis will do excellent with those as well.My suggestion is to read the description fully and know what you are getting and what you aren’t. If your reading experience will be destroyed because this doesn’t have (nor claim to have) a usb-c, then this isn’t the ereader for you.If you want it to be like a tablet or smartphone or computer, this isn’t the ereader for you.But if you love reading and buy this for what it’s made for, I can recommend it. Definitely look into getting a discount by trading in any unused kindles, and take advantage of the free Kindle Unlimited and Audible while they are available to offset the cost even more.',
     'I received this new Oasis yesterday. I plugged it in so that it could fully charge. As I was setting it up, I watched battery life rapidly decline from 100% to 96% in a matter of minutes. As a test, I left it asleep (no reading/downloading/etc) for ~24hrs. The battery is now at 19%. This is completely unacceptable. Amazon advertises this model as being able to hold a charge for weeks. This experience has demonstrated that a full charge will not even last 48hrs. I cannot in good conscience recommend this product.',
     'So I\'ve been using a Kindle Paperwhite since 2014 and absolutely loved it.  Despite it being five years old, it still worked great and has been a pleasure as a reading device.  I\'ve been debating the idea of upgrading to a new Kindle for a few months- and a few weeks ago Amazon had a really nice deal that allowed you to trade in your old Kindle for twenty-five bucks AND get 25% off the purchase of a new Kindle.  So, despite the fact that my old Paperwhite worked just fine, I decided to upgrade to the brand new 2019 Kindle Oasis.  I liked the idea of the color-changing LEDs for nighttime reading plus the benefit of having it be waterproof for when I read at the beach.  I placed my order and shipped my old Kindle back to Amazon.I\'ve been reading with my new Kindle for about two weeks, and my reactions have been mixed.  In some ways, the Kindle Oasis is definitely an upgrade over my old Paperwhite.  In other ways, it seems like Amazon swayed too far from the formula of what makes their e-readers great.  For the sake of this review, I\'ll be comparing the performance of the new 2019 Oasis to my old Paperwhite. I\'ll also make comments about how the Oasis compares against the current Paperwhite, which is likely a much better option for the vast majority of people seeking an e-reader.  It should be noted that I also ordered Amazon\'s nice Merlot leather cover... I\'ll review that too.Battery Life:Some people have complained about the battery life of the new Kindle Oasis.  I\'ll say that the battery definitely doesn\'t last as long as a Paperwhite.  My old Paperwhite\'s battery was still excellent, even at five years old.  My old Paperwhite had to be charged every 5-6 weeks based on my use.  After two weeks of reading, my Oasis\'s battery says that it\'s at 52%.  It\'s not a big difference, but it is noticeably less than the much cheaper Paperwhite.  (That said, I think the larger screen that likely consumes more battery life is well worth the fact that I\'ll have to charge it every four weeks verses six for the Paperwhite)  For the price premium, it would have been nice if Amazon included a battery that held a charge at least as long as the Paperwhite though.The LEDs and Night Mode:This is perhaps the best upgrade between my old Paperwhite and the new Oasis.  I often read before bed- and tend to do so with the lights off so that my wife can sleep.  With my old Paperwhite, the blue-hue LEDs were not easy on my eyes when reading in the dark.  That has all changed with the Oasis and it\'s night mode.  It allows you to change the LEDs from a blue hue to a yellowish hue that makes it a lot more comfortable to read in the dark.  I LOVE this feature and might even argue that the price premium of the Oasis is worth it just for that feature.  It\'s fully customizable so that you can find the color/hue that works best for you.  You can also schedule it so that it automatically switches at a certain time.  That\'s handy, even though it only takes about five seconds to switch it manually.Speaking of the LEDs, there is one feature that drives me nuts about the Kindle Oasis.  The auto brightness feature is extremely annoying.  It\'s extremely sensitive and seems to constantly auto adjust even when the room\'s lighting is consistent.  Over the first few hours of reading in my dining room, the auto brightness consistently changed over and over again ever thirty seconds or so- which is extremely annoying when you are trying to read.  My solution was to just turn off the auto-brightness setting.  To me, this is inexcusable in a premium e-reader.  My 2014 Paperwhite\'s auto brightness setting worked fine.  Somehow with all the extra features and new design, Amazon made this feature less user-friendly in the Oasis.Comfort / Basis Design:Okay- this is purely a subjective topic- but I think that the overall design of the Kindle Oasis is far inferior to the Paperwhite.  The fact that there is a large bump-out on the back for the battery along one side means that the Kindle is not balanced in your hand as you read.  My old Paperwhite- and the current one for that matter- was 100% balanced when held in one hand.  The Oasis isn\'t balanced- which means that as I read, I\'m frequently distracted by the fact that the devide is leaning to one side or the other, depending on orientation.  To add to this issue, the Oasis seems to be a lot heavier than my old Paperwhite.Response / Screen Response / Display:This is something that is, for the most part, is vastly superior compared to my old Paperwhite.  The touch response of the Oasis is lightning fast in terms of page turns, when you are browsing your library, or looking for a new book in the Kindle Store.  There is one exception: It\'s annoyingly slow when you first unlock it and have to slide your finger along the bottom.  In terms of the display quality- it\'s crystal clear, crisp, and impressive for an e-reader.  The larger 7" display might not seem like a large upgrade over the Paperwhite\'s 6" display- but its makes a big difference if you use your Kindle regularly.  Now that I\'m used to a 7" screen, the Paperwhite\'s smaller display seems tiny- even though it worked just fine for me for five years before I upgraded.  Lastly, the page turn buttons are user-friendly and well-designed.  You can also use the touchscreen to turn the pages, but I found that the buttons were more comfortable to use.Inexcusable Drawbacks:First, you get a charger cable, but not the wall outlet adapter... Considering that you\'re buying a premium e-reader, that\'s just ridiculous.  You shouldn\'t have to pay an extra twenty bucks to buy this- it should be included.  Seriously, how much more could those little chargers cost Amazon to include?  Second, I understand the advertising on the cheaper Paperwhite.  Why must I pay an additional twenty bucks to avoid ads on a two hundred and fifty dollar e-reader?  Really- the fact that these two things cost extra is inexcusable.Lastly, I want to comment about the Merlot Leather Cover that Amazon sells.  This isn\'t a review on the cover, but a comment about how the design of the Oasis really makes it hard to design a decent cover.  I debated on whether or not I should buy it or if it was even worth the price that Amazon wants for it- but decided to go for it considering that I\'ll probably keep this e-reader for five years or so before upgrading again.  That said, I really don\'t like it because it doesn\'t fit the Oasis very well.  Sure, the Oasis fits snugly into the case, but when you open it and fold the cover back, the binding isn\'t tight so it flexes and moves a little as you read.  In addition, because of the Oasis\'s battery notch in the back, there is a 1/4" gap between the front cover and the actual Oasis for about 60% of the Kindle back.  The causes the binding to shift even more- which is annoying.  This never was a problem for my Amazon-brand Paperwhite case from 2014.  Again- this is likely more due to the design of the Oasis than the design of the cover.Overall, you really need to consider if the Oasis is worth spending twice as much as a Paperwhite.  If you read A LOT and would benefit from the LEDs that change from blueish to yellowish, then the Oasis might be worth it for you.  If you don\'t really care about the color-changing LEDs, then the Paperwhite is likely the better option.  Most of the best features of the Oasis can be found in the current Paperwhite.  They both are waterproof, they both have great displays, they both have bluetooth audio capability, and they both have great battery life (the Paperwhite is likely even better than the Oasis).  Unless you are a serious daily reader- or can take advantage of a deal like I did, the Paperwhite is likely the e-reader that makes more sense.',
     "I have the previous generation oasis as well (on the left side in the pics) and wanted this one for reading at night. Overall there's not many differences between the two, so if the light tone customizability isn't important to you I wouldn't particularly recommend this one over the 9th gen. However, the lighting is noticeably more even with the 10th gen (my older one visibly fades from one side to the other) and there's a ton of variability in the tone of the screen. Overall, for me it was worth it, but your mileage may vary if you don't read in a dark room (so as not to wake the spouse) before bed very often.",
     'For the past few years, Amazon has seemed content to follow the e-reader pack rather than lead it and provide true innovation in its Kindle lineup. This version of the Oasis is no exception. While this latest Oasis adds the option for warm (amber) light, which is a plus for me since I tend to read a night, Kobo and Nook have had this feature for years. Amazon touted that its Oasis and now Paperwhite are “waterproof.” Big deal. Kobo did that in 2014. A 7” screen on the Oasis version 2 in 2017! Again, Kobo did that in 2013. The ability to change the boldness of fonts and provide some customization was provided by Kobo back in 2011. The Kobo Forma, an 8-inch radically different e-reader, shows what REAL innovation is. Go take a look at it.Let’s talk pricing. $249 (with Special Offers) $269 without them. The top of the line Nook is $199. And only Amazon makes you PAY to have an e-reader without advertisement. Let’s be honest, that’s what “special offers” are, ads.The Kindle ecosystem is second to none, unmatched by Kobo or even Barnes and Noble. That’s what keeps me with Kindle. It would be nice, however, if their e-reader line-up matched their industry leading eco-system. The big change between the Oasis version 2 and version 3 is warm light. Hardly innovation. Is it worth the upgrade? You need to make that decision. The screen is truly beautiful and evenly lit, the automatic light adjustment (including amber-warm light) is customizable and works perfectly, the software is excellent, and page turns are lightning fast.But wait, the Kindle Paperwhite is now available in Twilight Blue! Now that’s some innovation, LOL!',
     'I have never had an e-reader before. I used to read a TON, but then I grew up and life happened, so wanted to get back in to it.I purchased both the Paperwhite and the Oasis. The Paperwhite seemed like a great device, but I could tell immediately how much more my eyes liked the larger screen on the Oasis along with the warmth feature. The warmth feature was the biggest factor for me, as it made it look much more like an actual page out of a book. I\'ve included a picture of the Paperwhite (on the right) and Oasis (left), both set at the same brightness, but with the Oasis\'s warmth setting on. You can also see there is no white Kindle logo on the Oasis, which I found ever so slightly distracting on the Paperwhite. The quality of the screen on the Oasis is also much better than the Paperwhite - text is more clear and crisp. If you commute a lot or size is important to you, Paperwhite is definitely the way to go.I was really overwhelmed with the Oasis at first, just because it was so new to me. I\'m pretty good with new tech, but the whole environment was slightly overwhelming because it\'s not just as simple as getting a new device on a platform you\'re already used to (ie, Windows, Android, Apple, etc). Once I got past the learning curve, I started to actually like it a bit. However, the way the Kindle sorts and handles your books could be much better. You can organize things in to \'Collections\', but it still doesn\'t feel like enough. I recommend looking up Calibre and going from there.My biggest gripe is the ergonomics of the Oasis. Although it\'s not much heavier than the Paperwhite, it feels like it because of the shape of it. It just feels heavier because of the weight distribution towards the center, and is awkward to hold with that bump/excessive weight distribution that sticks out. I am a 5\'9" woman with \'normal\' sized hands, so I can\'t even imagine how this would be for someone with smaller hands. I bought a case immediately because the shell is ridiculously slippery, and in my opinion, a horrible choice of material for something you\'re going to hold for hours. Looks pretty, but not very functional for an e-reader. I bought the \'Ayotu Skin Touch Feeling Case\', and it is awesome. I ordered a couple of others and this one stood out among all of them big time.Last gripe is that the screen is pretty slow and laggy at times. I know it\'s an e-reader, but it\'s a very expensive one that doesn\'t do anything else (which to clarify I am absolutely fine with BUT, see next point), but at that price, it should really be perfect.A positive feature of this that is nice is that you can flip the device around and the screen flips with you, so if you are right or left handed or just want to switch sides during reading, that is super helpful.I do like it, but am considering whether or not I am going to keep it due to the ergonomics alone.',
     'The bigger format is welcome. It adds some to the physical size and weight, but for these mature eyes, I think the trade off is positive. I often read laying on my side and really like that the view flips so I can tent the device laying on either side.  I’m a bit mixed about the bump out. I’m leaning to like the totally flat design of my prior Kindles, but think I’ll get used to it. The touch screen is noticeably better, but it could hardly be worse and is still not as reliable or responsive as one would expect. The format of the pass code entry is noticeably bigger and helps to avoid entry errors. This charging cord is too short to charge while reading. This is a huge disappointment as it looks like to buy a 6’ cord is pretty expensive.  A comment the a prior iteration of this post references finding cheap 6’ Cords. Perhaps. But I suspect Amazon chose a cheap manufacturing option and will soon be in a fix with this battery. Other reviewers were annoyed that this does not use a USB-C. I travel a lot so cutting down on device clutter is important. Right now my iPad and laptop have the new USB-c and I’m sure my next phone will, too. But I’ll still need an older usb for other rechargeables like ear pods, flashlight and speaker. THE KILL FACTOR: battery lasts about 4 days with modest use as opposed to ‘several weeks’ as advertised. This is replacing a well used Voyage that had very good battery life.  It looses 2-3% while turned off for a few hours. I tried 3 times to return it in the normal way. It seemed like I was able to return for replacement, but I never got a shipping label. Finally talked to a tech who said someone would call to ask me some questions. I gather they are trying to determine if this is an isolated problem (I notice several other battery life complaints) or a bigger problem with the battery design or a batch of batteries. They did promise a replacement in 4 days, which is pretty poor since I’m a prime member.  One would also think they’d be very responsive as this may be a really big problem, but apparently they are not very anxious to please.UPDATE:  A replacement was received 5 days ago.  It came essentially in a "brown bag," so I was a bit suspicious that it is not new.  But trying to be optimistic and really wanting this new Kindle to be a keeper, I reasoned that if it was a repaired one, perhaps it works.  In first couple of days, the battery life dropped like a rock.  Three days ago, I recharged and started a new book.  When I quit reading sometime after midnight today, I was 56% through the book and there was 30% power. I checked at 8:30am (after no usage for several hours) and the battery had dropped to 23%.  I just checked again at 4:45pm after no usage and the battery shows 21%.  What are the odds that I get 2 lemons?  Seem pretty low to me.  I read some of Amazon\'s remarks to complaints about the reader taking extra time when new to index and load books, it needing to be restarted, etc.  I do not recall this happening previously, so I am suspicious about this explanation. Also, a basic of product design is to warn of dangers and how to avoid them. If usage is not intuitive, the manufacturer should instruct.  One way or the other, it seems like Amazon has failed with at least some of this model.  But I\'m going to recharge and give it a chance.  At this point I am very discouraged and really suspect about the battery design and the reviews that say they love this new Kindle.The 2nd Kindle was returned due to almost identical abysmal battery performance.  I keep checking back, hoping that there has been a recall or fix on this. As a voracious reader, I’d love to have the warm light feature. Likewise, I found several other features attractive. It appears, for many, battery life remains a significant problem and Amazon remains silent.']




```python
import pandas as pd
```


```python
dat_r = {'review':all_reviews}
dat = pd.DataFrame(dat_r)
dat
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>review</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>This is my 11th Kindle. Their last Oasis model...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Pros:__________•  It’s small, provides basical...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>I wrote a lengthy critical review of the 2017 ...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Your browser does not support HTML5 video.\n\n...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>I received this new Oasis yesterday. I plugged...</td>
    </tr>
    <tr>
      <th>5</th>
      <td>So I've been using a Kindle Paperwhite since 2...</td>
    </tr>
    <tr>
      <th>6</th>
      <td>I have the previous generation oasis as well (...</td>
    </tr>
    <tr>
      <th>7</th>
      <td>For the past few years, Amazon has seemed cont...</td>
    </tr>
    <tr>
      <th>8</th>
      <td>I have never had an e-reader before. I used to...</td>
    </tr>
    <tr>
      <th>9</th>
      <td>The bigger format is welcome. It adds some to ...</td>
    </tr>
  </tbody>
</table>
</div>




```python
dat.to_csv("kindle_reviews.csv", index=False)
```

### 하나의 제품에 대하여 작성된 리뷰들을 여러 페이지에서 가져오기


```python
sel_all_reviews2 = driver.find_element_by_xpath('//*[@id="cm_cr-pagination_bar"]/ul/li[2]/a')
sel_all_reviews2.click()
```


```python
page = driver.page_source
soup = BeautifulSoup(page, 'lxml')
soup.title
```




    <title>Amazon.com: Customer reviews: Kindle Oasis – Now with adjustable warm light – Ad-Supported</title>




```python
all_r2 = soup.find_all("span", class_='a-size-base review-text review-text-content')
all_r2[0].text
```




    '\n\n  I have always been of the belief... if you are willing to pay a bit more for a product - and as long as you use it regularly, its worth every penny.  I am fortunate to have bought this new Oasis with a generous Birthday gift card from my wife.  My early impressions are WOW.  The 7 inch screen makes a huge difference.  This Kindle is perfectly made with the reader who holds it in hand while reading in mind.  Now, the new warm light is great.  You can schedule it to kick in at a specific time, you can tell it to go by sunrise and sunset, or - simply set it manually.  I have chosen the latter.  By my taste (and use this as a guideline if you wish)  I have brightness set to 15.  I have set warmth to 12.  I use the "bookerly" font set at bold setting number 2, and size - number 6.My only complaint is that (I hope AMAZON is listening)  its time to replace the same screensavers that have been used for years.  I think at this price point, the user should have a choice.  The currect book reading\'s cover is one - perhaps user selected images another.  I have the ad free version and I hold it in hand while reading.  This is the most comfortable reader yet in terms of comfort holding in one hand for hours while reading.  Its worth every penny if you read most days.  Now, battery life seems to be a bit of a disappointment but still - I cannot stir away from giving this genius device 5 stars.  I also recommend the leather feel stickers that are available for the back that will eliminate the issues people have had with the "slippery" issues of the past.  This is the KEEPER of Kindles.  I have owned most - snce the keyboard model.  Love it!!!\n\n'




```python
all_reviews2 = []

for one in all_r2:
    tmp = one.text
    review2 = tmp.strip()
    all_reviews2.append(review2)
    
print("리뷰 개수 : ", len(all_reviews2))
print(all_reviews2, sep='\n')
```

    리뷰 개수 :  10
    ['I have always been of the belief... if you are willing to pay a bit more for a product - and as long as you use it regularly, its worth every penny.  I am fortunate to have bought this new Oasis with a generous Birthday gift card from my wife.  My early impressions are WOW.  The 7 inch screen makes a huge difference.  This Kindle is perfectly made with the reader who holds it in hand while reading in mind.  Now, the new warm light is great.  You can schedule it to kick in at a specific time, you can tell it to go by sunrise and sunset, or - simply set it manually.  I have chosen the latter.  By my taste (and use this as a guideline if you wish)  I have brightness set to 15.  I have set warmth to 12.  I use the "bookerly" font set at bold setting number 2, and size - number 6.My only complaint is that (I hope AMAZON is listening)  its time to replace the same screensavers that have been used for years.  I think at this price point, the user should have a choice.  The currect book reading\'s cover is one - perhaps user selected images another.  I have the ad free version and I hold it in hand while reading.  This is the most comfortable reader yet in terms of comfort holding in one hand for hours while reading.  Its worth every penny if you read most days.  Now, battery life seems to be a bit of a disappointment but still - I cannot stir away from giving this genius device 5 stars.  I also recommend the leather feel stickers that are available for the back that will eliminate the issues people have had with the "slippery" issues of the past.  This is the KEEPER of Kindles.  I have owned most - snce the keyboard model.  Love it!!!', 'DEFECTIVE - the battery life is horrible. After two calls to support and two software updates I did a test. I put it to sleep for one hour and the battery declined from 72% to 54%; I read for 5-8 minutes and it declined 5%. A third call to support was: don’t call us, we’ll call you in 3 to 5 business days. I was so looking forward to an upgrade, but this stinks.', "I am bedridden and I rely heavily on my kindle to keep me from losing my mind. I bought this new one because my old one is dying. It's a 2nd generation and I've used it constantly for years)I'm going to buy another paper white and use it until it dies too.  I really hope they continue to make them in perpetuity since the oasis is far too hard to hold. I have advanced arthritis (RA and OA) and holding the oasis is nearly impossible for me and painful too.", 'I have had the Oasis 2017 for one year now.  This new 2019 updated iteration really caught my eye based on the warm lighting feature.  Having used it today for several hours, I can say I am so pleased and exited I made the leap and upgraded.  The device is very quick and snappy.  The lighting is 5 stars.  The buttons have a nice click feel to them.  It feels so nice in the hand (no case).  Now, for the warm lighting.  It has improved an already incredible device even better.  Please reference my 3 pics showing the warmer tones.  One pic shows the lighting levels for all 3 pics.  It is definitely easier on the eyes and makes the black text stand out even more.  The screen is very sharp and crisp.  The lighting setting in the pics mimics the color of pages in a hardback novel.  No more harsh blue light for me.  I intend to use the warmer lighting all day and night regardless of background lighting.  The difference is that marked.  Happy reading my Kindle friends :)', "When I upgraded my Kindle to this newest model, I got an offer to trade in my most recent model for up to $50. My older model was still in great shape and works perfectly, so I didn't hesitate. Today, I got a note that said I would be paid only $5, but that I could get a 25% discount on a new Kindle! I just spent $250 on a new Kindle, and you want to pour salt into my wound?", "I've had the previous gen Oasis for almost 3 years and thoroughly enjoyed it. I have Kindle unlimited, so for what I got for my old Oasis on eBay and 6 months of unlimited for free, the new Oasis  cost me under $50. That's a no brainer.The new Oasis is only an e reader. Yes, that's no secret. Uses older usb? I charge about every 10 days and I use the device every day. I let it charge overnight, so I just don't see the big deal about usb-c.Cases? My old case physically  fits but doesn't turn the device off. It will, however, turn itself off. When you open the case you must push the power button. Not a big deal, but I bought a new leather case on ebay for $10, made for this new Oasis.Kobo, nook? I've used them both and while each may have a feature up on the Oasis, neither can provide the overall positive reading experience the Oasis does.If you can afford the price, the Oasis is the way to go.", "I was greatly disappointed in my Oasis 2019 model.  I was under the false impression that it would adjust to the different lights itself.  And when I adjusted it, it really wasn't much different than reading on my regular kindle when I turn down the brightness to read in bedMy device also had a visable line going down the middle, this was distracting when trying to read.My last issue was when I purchased this prior to release on July 4th,  the promo was 3 free montjs of kindle unlimited,  so when my billing cycle was up on July 20th, I canceled my subscription knowing my new kindle was coming and I was getting 3 free months.  But I was informed that the Oasis only came with 1 free month.  I wish I would have screen shot the promo when I pre-ordered mine.  I had books in my kindle unlimited that are no longer part of the subscription and will cost me more thsn my free monthThe device is light, the design was nice,  and the water proof is very misleading,  But for the cost, I was unsatisfied, felt it wasn't as advertised and did not offer all the bells and whistles as promised", "Way to go Amazon! Put an ugly bright Amazon logo on the cheaper model so I purchase a more expensive one! All that aside, I'm very happy I chose the Oasis. By far the best Kindle yet. I get very attached to my kindles and have a hard time choosing when I need a new one. When my kindle keyboard broke I purchased the Voyage and absolutely loved it. I was so disappointed when I broke it last week and found Amazon no longer makes them. So the decision began.....I prefer buttons but wanted them on both sides, and I wanted waterproof.  I didn't care for the design of the oasis (I didn't want to have to flip it every time I change hands) but I did like the fact it had some buttons and the warm lighting I felt was something I would use. But the price!!!! I considered the paperwhite but there was no way I was going to look at the logo all the time. I would have bought the basic (with a black unobtrusive logo) but it wasn't waterproof. So....that left 1 option...Here are my list of pros and cons:Pros are buttons, no branding on the front screen, waterproof, warm lighting, easy to hold, the screen is beautiful and easy to immerse yourself in reading.Cons are battery life, buttons are a bit noisy (make a clicking sound that might annoy your parter at night), metal casing is horrible to hold naked which ties in with the next con. If your going to make an odd shaped device then make a cover for it that doesn't obstruct holding it like it's designed to be held! Come on Amazon, something as simple as a case and you can't get that done in 2 years? This forces you to buy 2 cases if you want to hold it comfortably. Also the screensavers are the ugliest things I've ever seen! I purchased the one without ads so I could get it sooner and if I would have known how ugly the screensavers looked I would have waited. Why can't you just put the picture of the boy under the tree?All said, I do believe that this is the best kindle yet. With the 25% trade in that Amazon is offering right now and the 3 months of kindle unlimited, that brought the price down to just above the regular price of the paperwhite. I recommend going with the one with ads which look better than the screensavers. If you can afford it, it is definitely the best kindle ever made.", "This is my fourth or fifth Kindle. I took advantage of the Prime Day 2019 sale plus buy back to get the Oasis at an affordable price. The Kindle I sold back to Amazon was a first or second generation Kindle Voyage. I was tremendously excited about the grip on the Oasis because it was something that I felt the Voyage needed. I was also excited about it being waterproof; this feature would allow me to take it to the public pool without worry.  I had expected that there would be a suitable Amazon cover for it but I can't seem to find one that would allow me to read the way that I generally read.Here were my problems:1. The screen and item are much smaller than I expected. No, I did not read and measure out the dimensions but every Kindle I have had has had about the same size area for reading. Not the Oasis. To get the same feel, I have to turn it sideways but your options are to either have it sideways or up and down which leads me to ...2. The screen orientation does not change automatically like a phone. You either have to set portrait or landscape. It will then automatically flip 180 degrees in that orientation. I understand why they would choose to do it this way but a better option would be to have a quick to reach toggle that makes it stick. Right now I have to do five presses to switch between portrait and landscape. If I read in bed and need the grip, I have to change it to portrait mode. At the gym, I have to change it to landscape (it's much more stable on the cardio machine holds with the grip toward the ground; otherwise the grip slants it).3. I don't know if I got a bad one but battery life sucks even without use. I have it in airplane mode 99% of the time (which means Bluetooth is turned off) and the light setting is at 11. I used to get approximately 3 weeks of life out of the Voyage. I am not getting a week out of the Oasis and I have been using it significantly less than previous months (it's been a slow reading month).4. The thing is so small and thin that the grip doesn't do much to make it easy to hold. The first problem I had was that holding it on such a way that I could somewhat use the grip made the buttons on the thing awkward to reach. Thankfully they do have the option of reversing the buttons.5. The power button is way too sensitive. I tried using this at the gym initially in portrait made. I naturally hold this thing in my left hand so I placed it on the machine shelf with the buttons and grip toward the left. This means the power button is on the bottom. Just placing it on the shelf turned it off. I had to flip it around. Okay, I thought, stupid me. Nope, I constantly turn this thing off and on just handling it6. Which brings me to, why is this thing so slow to turn on? When I've actually wanted to turn it on (until I realized that it was just super slow), I ended up turning it off again because I pressed the button again thinking I didn't get it the first time. The Voyage was practically immediate for me between button press and the screen requesting a swipe.I have nothing nice to say about it other than all the other nice things I'd say about any Kindle. I have loved my previous Kindles though each one (of course) could use improvements. Amazon is good about improving the Kindles but this one was a fail for me.I have two days to return this thing and I am not sure what I am going to do. Am I going to return to get another Kindle Voyage? I only got $50 for my Voyage but there's no way to get it back. Perhaps I have a defective one and I should get an exchange, specifically I think the battery is problematic on my device.", "I didn't like the feel of this device and I tried but didn't like the warm lighting.  I guess all in all I am okay with the white/blue of the other kindles when it really comes down to it.  When I used the warm lighting I would catch myself making the screen brighter.I purchased the official case and thought that it was a nice case.  I wouldn't suggest the genuine leather if you carry this in your purse.  It will be destroyed/scratched up in no time.  I understand that is how the leather is but I didn't like it.  I never realized how rough I am on my Kindle until now.I purchased this to replace my Voyage and ended up returning it for a Paperwhite.  I just didn't like the shape of it.  I liked that it would auto rotate when I switched hands though.  And I didn't like that it wouldn't sit flat on my desk without a cover folded back.I wish they would release a new Voyage or at least bring it back for those that love it."]
    


```python
import os, warnings
import re
warnings.filterwarnings(action = 'ignore')
```

사용자 추가


```python
soup.find_all("span", class_='a-profile-name')[-1].text
```




    'Christi S.'



평점 가져오기


```python
all_r2 = soup.find_all("div", class_='a-section celwidget')
all_r2[0].find("span", class_='a-icon-alt').text
```




    '5.0 out of 5 stars'



날짜


```python
tmp = all_r2[0].find("span", class_="a-size-base a-color-secondary review-date").text
texts = tmp.split("on")
texts[1].strip()
```




    'July 29, 2019'



지역 정보


```python
tmp = all_r2[0].find("span", class_="a-size-base a-color-secondary review-date").text
texts = tmp.split("on")
texts[0].strip()
```




    'Reviewed in the United States'



한 페이지의 정보 가져오기


```python
all_r2 = soup.find_all("div", class_="a-section celwidget")

all_users = [] # 사용자
all_ratings = []  # 평점
all_dates = []  # 날짜
all_regions = [] # 지역
all_reviews = [] # 리뷰

for one in all_r2:
    user_one = one.find("span", class_="a-profile-name").text
    all_users.append(user_one)  # 사용자 추가
    
    rating_one = one.find("span", class_="a-icon-alt").text
    nums = re.findall("\d+", rating_one)[0]
    all_ratings.append(nums)  # 평점 추가
    
    date_one = one.find("span", class_="a-size-base a-color-secondary review-date").text
    texts = date_one.split("on")
    data = texts[1].strip()
    all_dates.append(data) # 날짜 추가
    
    region_one = one.find("span", class_="a-size-base a-color-secondary review-date").text
    texts = date_one.split("on")
    region = texts[0].strip()
    all_regions.append(region)
    
    review_one = one.find("span", class_="a-size-base review-text review-text-content")
    tmp = review_one.text
    review = tmp.strip()
    all_reviews.append(review)  # 리뷰 추가
    
print(all_users)
print(all_ratings)
print(all_dates)
print(all_regions)
print(all_reviews)
```

    ['Marina', 'Amazon Customer', 'Wook', 'Monica186', 'Don P.', 'Michael A Kelley', 'Douglas Henson', 'SK', 'Mydogsmom', 'Koi girl']
    ['5', '1', '3', '3', '5', '5', '5', '5', '5', '5']
    ['July 15, 2020', 'March 15, 2021', 'September 17, 2019', 'November 20, 2020', 'October 25, 2019', 'April 10, 2021', 'February 16, 2021', 'October 24, 2020', 'April 5, 2020', 'January 14, 2020']
    ['Reviewed in the United States', 'Reviewed in the United States', 'Reviewed in the United States', 'Reviewed in the United States', 'Reviewed in the United States', 'Reviewed in the United States', 'Reviewed in the United States', 'Reviewed in the United States', 'Reviewed in the United States', 'Reviewed in the United States']
    ['Your browser does not support HTML5 video.\n\n\n  \xa0This is my second kindle. My first kindle I got in 2011 and it’s the one with the keyboard. Even though it’s still in perfect condition and has been lovely these past 9 years, I can’t tell you how happy I am to be holding a kindle that has a backlight AND is touch screen. I feel like I’m coming out of the dark ages. This device is so beautiful. I love the side buttons. The price is a bit much for an e-reader but you can feel and see the quality when you’re holding this device. I expect to have this baby for the next 9 years. If you can afford it and are an avid reader, go for it!', 'I had not used the kindle for a while and when I started using it more frequently, the button that turns pages stopped working. I googled to find a solution and tried what was suggested. It worked for a while but started doing it again. when I decided to get help from Amazon I found out that not only Amazon does not replace the device, but eve stops support after a year. It is an expensive device and it should have better support. Shame of you Amazon!!', "So, I carry my Kindle Oasis everywhere, including meals, where one of the page turn buttons got stuck in the down position.  This is death for a kindle.  So, while weighing my repair options, I whipped out my phone, and ordered a new one.  Huge Mistake, based on my faulty assumptions (and the fact that the page is poorly laid out for mobile), because:1) It doesn't have cellular connectivity (even though I got the high priced one).  This is a killer for me.2) Because it was another Oasis, I assumed my existing cover would work for it, and it doesn't:  A) It doesn't attach securely, constantly falling off;  B) When it is attached, the kindle seems to detect cover-closed and is constantly turning itself off;I don't want to return it for a refund, because I feel this is my fault as much as it is Amazon's, but I am massively disappointed in this Kindle purchase (I have several).  It's sufficiently unusable that I'm re-using old ones...", 'The lighted screen is great - best of the 7 Kindles I have owned over the years. The touch screen is fine, though nothing to write home about. The battery life is disappointing compared to my Kindle Voyage, and the Oasis is not comfortable to hold in my hand. I had hoped that I would get used to it, but it has been more than a month, and I still prefer the Voyage. I hope they bring back the Voyage, or re-design the Oasis so that it is more comfortable in my hand and will fit in my smaller handbags the way the Voyage does.', 'I was trying to decide whether or not to buy the new Kindle Oasis; It\'s not cheap, and I liked my Paperwhite. However, I read another review praising the "warm" lighting feature and I was intrigued. I finally decided to get it (not only for the light, but the different design and larger screen,) and I am so happy I did!The light: I thought the warm-light thing would be sort of a gimmick, but it\'s really not. IMHO it is a much more pleasant reading experience than the cold white of my old Paperwhite. Amazon would do really well to put it in all their models. I don\'t really like the auto-brightness feature on *any* device though, and it\'s no different here; I just adjust the lighting manually.The design: The buttons and weird shape are actually really well placed. Because of the auto-rotate function, I can hold it in either hand and have the page buttons right under my thumb, and the \'bump\' on the back actually makes it easier to hold, since the buttons are on the same side.The battery: The battery isn\'t as good as my paperwhite. Don\'t get me wrong, it\'s still great, but with the added lights, the battery is used faster -- it still lasts several days for me though!Miscellaneous: I bought mine bundled with the case/cover, and I *highly* recommend doing this. Not only does it protect the screen, but the Oasis automatically turns on/off with the magnetic cover.Overall I am very pleased with the Oasis, and my eyes thank me for it ;-)', "After many years using my wife's decaying Paperwhite, I anxiously awaited my 2020 XMas present: a new Kindle Oasis.This is a thing of beauty. I love the bigger screen, which is much better for my aging eyes. The metal backing feels so cool to the touch. The light sensor and backlit customization complete the package.I was in e-book heaven. Until the day I received my Oasis cover.I received my Ayotu Fabric Soft Case on a Saturday afternoon. It fit my Oasis great, and it eased my fears that I'd accidentally damage my new Oasis. I placed it lovely on my nightstand. Life was great!That night, my wife and I celebrated our wedding anniversary #11. The meal I picked up from our local restaurant was lovely, the company was lovely. Except that my wife seemed a little nervous. After a few glasses of wine, and after we finished our last bite of dessert, she couldn't wait any longer.She revealed that our puppy had used my Kindle as a chew toy.While my wife was taking a shower, and while I was picking up our meal, the puppy was in our bedroom. Bored. So bored, that instead of chewing the numerous chew toys we had spread out across the bedroom floor, he had decided to look elsewhere for something to chew. And he found it on my nightstand. My beautiful newly covered Oasis.Needless to say, this put a damper on my happiness that evening. Yet again, it made me curse the puppy's name.So please learn from my mistakes. Nothing in the documentation, or the Amazon web page, mentions that the Oasis is NOT PUPPY PROOF. It cannot withstand the pressure of a 8 month old puppy jaw.  It does not emit puppy repellant. I will continue to wait until Amazon comes out with a puppy proof Oasis, our until someone makes a puppy proof cover.", "Okay... Long story short: I have been looking at the Oasis here on Amazon and elsewhere for months... MONTHS! I have read reviews, I have looked at specs, I have looked at advertisements and videos... Did I mention that I have been doing this for months? Here, in brief, is what I learned from all of this research: the Oasis is a reader not much different from the Paperwhite I have been using. The price is higher. Is it worth the price? The screen is too reflective. The Paperwhite is just right. The lights are brighter. Well, so are the Paperwhite's. There is warm lighting on the Oasis. From the pictures/videos I could not really tell what that means. Well, so I did this for months, as I mentioned before... What exactly is the appeal? Oh, a larger screen? It didn't really look like it was all that much bigger... besides, the Paperwhite screen was just great. So??? So, I finally ordered one and here is what I found: I opened the package, pulled out the Oasis, I turned it on... I FELL IN LOVE! OMG! The Oasis just feels so luxurious in my hand. I thought that little thick side looked kind of goofy before. I now see it as a sign of brilliant design. The page buttons are a joy to use and I almost never have to touch my screen anymore (for menus and library only now). The lighting is spectacular and the warm light in low level light just makes the screen so much easier to read. The display is crisp and clear. I had read where some folks where having problems with page bleeding from one screen to the next and I have experienced this when it is very cold and the Oasis is first turned on... It seems to need a moment to warm up and then the bleeding goes away... NOT an issue/problem. The display is not any more reflective than any other Kindle I have used in the past. Oh and so very light! I would say my Paperwhite, with a cover, is easily three times heavier. That may not seem like much and in practical terms it is not that big a deal, but oh how that light weight adds to that feeling of  luxury. And then there's that page flip thing... As you sit and hold the Oasis in your right hand all comfy and cozy feeling all pampered while you read and then have the dog jump up on the couch next to you wanting some attention... Well, just put that Oasis in the left hand, freeing up your right hand to pet Fido, and the display flips over so that the Oasis now fits just as easy in the left as it did the right hand. That, my friend, is yet another bonus of amazing design and luxury! Do I think the price is worth it? Tuff question. My Paperwhite is very affordable and well worth every cent I spent on it. I love that little reader. But, the luxury of the Oasis is just so incredible... For ME, in the end, I would say it was well worth it. Now, the one thing I should mention is that the battery life has not been as long as I expected it would be, but I have to admit that I am reading for hours longer that I did before too... That may very well be the reason it is not as long as I expected... So, I guess when it comes to battery life, your mileage may vary, as they say. My concluding bottom line would be: Absolutely the most luxurious thing I have every purchased and to say it's a pleasure to use is merely a faint echo of symphony of joy I feel using it!", "update 11/30sometimes there are bluetooth connectivity issues with my Bose headphones. It gets resolved after removing the device from oasis and adding it back.what i like1) Great technology which is very easy on eyes2) the warm light helps a lot and makes it feellike reading a book. To me this is the best feature, I would pay money for3) i love integration with good reads4) I don't find lock screen ad annoying at all5) switching between reading and hewring is easy6) very ergonomic, feels good holding in hand7) landscape mode is great but I wish there wad an easy way to do it8) sleeping on closing the cover(additional buy) is great9) screen lock with passcode is good10) easy integration with kindle store11) sync between app and device12) wordwise and making notes13) easy transfer of your books using other apps14) buttons feel great but I am still getting used to it15) I like to turn off wifi once my books are downloaded, to increase battery life16) dark mode is great but I love to read it without dar mode and with warm light17) I don't prefer a browser , the experimental browser isn't great, but I love that you can turn it off in settings18) can create profilesfor 4 children and one adult19) auto brightness is a great feature. it takes few seconds to change if environment changes from bright to dark. But from dark to bright it changes fast. I like it.20) I use bluetooth with my Bose headphone.Bluetooth works great.21) free 3 month kindle unlimitedI feel needs change1) change to usb c port2) reading while hearing( can do this on kindle app or fire tablet), I understand it is a technology limitation but please work on it3) auto landscape or easy switching to landscape, its hard to switch back going through settings4) I had to wait almost 9 days but it was worth the waitBest partI got it for $200 with almost $80 discount during prime day!", "So, I am an old Baby Boomer-and old school in so many ways-especially technology. I never thought that I would buy an eReader. But these are weird times that call for unusual and radical decisions. We are all shut in and trying to figure out how not to go insane. Well, I can vouch for the fact that this little gadget is very helpful in keeping me entertained. I don't have to worry about a virus coming in on a book delivery. I can access virtually everything with the push of a button. But the huge surprise is how much I love this thing! It is lightweight, easy to use, and even waterproof (so I can still read in the bathtub!) I know there are features I haven't figured out yet (and I hate that a printed manual was not included) I would love to try the audio feature but right now I am just thrilled to have so many books just a click away...", "Upgraded from 2-year old Paperwhite bc of blue light reduction for night reading, physical page buttons, and waterproofing.  Hesitated bc of expense but relented when price was deeply reduced at Black Friday.  I have to say it is a real and definitive upgrade over the Paperwhite.  Battery life has been much better than expected and it is just a much more solid device with a quality feel and display (and it should be for the exorbitant price, even with discount).  IMHO, there is no excuse for 8GB memory and a micro-USB connector in a late-2019, premium e-reader.  Is it worth the price difference over a Paperwhite?  It's hard to say; probably not if you're on a budget and/or you don't use your Kindle several hours a day, especially for night-time reading.  But it is undoubtedly a noticeable upgrade over the Paperwhite, at least for me ."]
    

여러 페이지에서 리뷰 가져오기


```python
all_users = [] # 사용자
all_ratings = []  # 평점
all_dates = []  # 날짜
all_regions = [] # 지역
all_reviews = [] # 리뷰

for one in range(2,7,1):
    time.sleep(3)
    
    page = driver.page_source
    soup = BeautifulSoup(page, 'html.parser')
    all_r2 = soup.find_all("div", class_="a-section celwidget")
    
        
    for one in all_r2:
        # 사용자 추가
        user_one = one.find("span", class_="a-profile-name").text
        all_users.append(user_one)
    
        # 평점 추가
        rating_one = one.find("span", class_="a-icon-alt").text
        nums = re.findall("\d+", rating_one)[0]
        all_ratings.append(nums)
        
        # 날짜 추가
        date_one = one.find("span", class_="a-size-base a-color-secondary review-date").text
        texts = date_one.split("on")
        data = texts[1].strip()
        all_dates.append(data) 
        
        # 지역 추가
        region_one = one.find("span", class_="a-size-base a-color-secondary review-date").text
        texts = date_one.split("on")
        region = texts[0].strip()
        all_regions.append(region) 
        
        # 리뷰 추가
        review_one = one.find("span", class_="a-size-base review-text review-text-content")
        tmp = review_one.text
        review = tmp.strip()
        all_reviews.append(review)
        
    # 확인
    print("user :", all_users[-1], "rating :", all_ratings[-1])
    print("review :", all_reviews[-1], end="\n\n\n")
    
    # 다음 페이지 클릭
    sel_next = driver.find_element_by_xpath('//*[@id="cm_cr-pagination_bar"]/ul/li[2]/a')
    sel_next.click()
    
print(all_users)
print(all_ratings)
print(all_dates)
print(all_regions)
print(all_reviews)
```

    user : James R. Van der Veen rating : 5
    review : As an old fart, an instruction and operations manual would be great. Also a trouble shooting guide would be wonderful. I had to return my first unit after spending 50 minutes with a very nice Amazon helper. She and I both agreed I needed a new one. Well, I hot the new one and had a lot of similar issues, but the issue is knowing how to use it. Now, after about 40 books, I've almost figured out how to use the damn thing. But I  read for 3 to 5 hours a night as part of my sleeping routine. I don't sleep well. I also use blue light glasses to cut the blue light hitting my eyes. My cell phone has this as an additional feature. Well, I've read a lot of books, all action/adventure, and I'm not sleeping any worse, but not a lot better. I think my problem is subject matter. I live in south Florida, have spent years in the Bahamas and Keys, and this is the backdrop to all of my books. So, I will now start searching of non-action/adventure style books. Might end up reading the Bible, but it's action/adventure most of the time on an even larger format.  So who knows??
    
    
    user : Kaniki rating : 3
    review : I like the new kindle oasis because of the backlighting (means I can read while my husband sleeps).  However, the battery life is just over two days if you delete the wi-fi info.  If you have the wi-fi data input, you cannot turn it off and on so then the battery lasts only about a day and a half.  Using airplane mode does not extend the battery much.  Really disappointing since I read for about two to six hours a day.  So that means at the most, the battery lasts 12 hours without recharging.  Again, really disappointed with the battery.  My first kindle battery lasted a month (without wi-fi on).
    
    
    user : Cindy Duncan rating : 5
    review : I was hesitant to upgrade from my 3rd generation kindle keyboard because of the lack of a keyboard but I LOVE this kindle. The touchscreen makes the keyboard unnecessary and the backlight feature is wonderful. I did want the side buttons which is why I chose this version. You can flip it over to use the buttons on either side depending on how you are holding it.  Or you can tap the screen to advance the page. But the combination of all those features for me make it the perfect upgrade and I don't regret it at all. Battery life seems fine to me, usually about two weeks with me reading a little every day. Seems to charge pretty quickly as well. Highly recommend especially for those with the older kindle.
    
    
    user : Alisha T rating : 4
    review : The only issue I have is you can't immersion read... You can't listen to audiobooks while also reading. I really miss that feature since I got use to it on the kindle app on mobile.  I also feel for the price your pay for the Oasis it should definitely be a feature that's why 4 stars instead of 5. I am hoping at some point kindle will upgrade this feature  I have had the kindle fire but the kindle Oasis is definitely a better option for the avid reader . I enjoy that it doesn't let you do much else but read. That way I won't get distracted by web browser and game play or apps. It's like carrying a million books in one hand. It really holds alot. I get constantly ask what the device is and people are always impressed with it . I like sleek and light weight feel.
    
    
    user : John J. Floro rating : 5
    review : I struggled to decide if I wanted to cough up the extra money for this e-reader, but I am so glad I did!  A few of the things I like about it are the 7" screen, the even and adjustable lighting, and the push button or screen tap features. However, the best feature, over my previous Paperwhite, is the fast speed of the processor.  I would never think the processor speed would make the reading experience much different, but it sure does. The battery life is as described.  I have only had it a week and have been through about 2.5 books (1 of which was an Audible book) and have only recharged it once when it went down to 30%. I love this thing!
    
    
    ['Worldwidehavok', 'JackandCyn1', 'Dave_5k', 'CWM', 'Zippy1643', 'David Rosenberg', 'Dave C', 'J. Reyes', 'Heather O', 'James R. Van der Veen', 'frank', 'AO', 'M.L. Powers, MS', 'Susan', 'astateprincess', 'LN', 'L.A. Blu', 'dontpanic42', 'Kindle Customer', 'Kaniki', 'Ronald L. Babb', 'Beauty Star', 'Edson W. Kempe', 'M. lewis', 'Jules T.', 'thisismaggie', 'Zike', 'Rmill', 'cristin', 'Cindy Duncan', 'Tabitha Smith', 'Kindle Customer', 'LGS625', 'Kep', 'Chris R. Johnson', 'Ginny L.', 'Cynthia Miller', 'Contrisger', 'Marcos Yturri', 'Alisha T', 'Erin Nicole Hollingsworth', 'Will', 'Kindle Customer', 'Linda Napoli', 'ila b', 'Bret', 'VERONICA', 'Kirsten', 'Douglas Meyer', 'John J. Floro']
    ['4', '2', '3', '3', '4', '5', '3', '5', '4', '5', '1', '5', '2', '1', '5', '3', '4', '4', '5', '3', '4', '5', '4', '5', '5', '5', '3', '2', '2', '5', '5', '3', '4', '5', '4', '5', '5', '5', '1', '4', '5', '5', '1', '4', '1', '1', '3', '5', '5', '5']
    ['April 25, 2021', 'August 29, 2020', 'October 21, 2020', 'June 17, 2020', 'October 10, 2019', 'August 26, 2020', 'January 14, 2020', 'October 20, 2019', 'June 22, 2020', 'February 22, 2021', 'August 14, 2019', 'March 24, 2020', 'October 26, 2019', 'December 12, 2020', 'August 21, 2019', 'January 4, 2020', 'January 2, 2020', 'January 11, 2021', 'March 25, 2021', 'June 4, 2021', 'December 26, 2019', 'October 20, 2020', 'August 23, 2020', 'March 29, 2020', 'January 6, 2020', 'October 12, 2019', 'May 25, 2020', 'December 5, 2019', 'January 3, 2021', 'December 11, 2019', 'April 5, 2021', 'November 28, 2020', 'August 5, 2019', 'August 10, 2019', 'April 20, 2021', 'April 27, 2021', 'January 28, 2020', 'January 28, 2020', 'April 1, 2021', 'June 21, 2020', 'October 22, 2020', 'January 5, 2021', 'March 25, 2021', 'September 28, 2020', 'January 25, 2021', 'July 17, 2020', 'February 4, 2020', 'December 27, 2020', 'August 28, 2019', 'January 18, 2021']
    ['Reviewed in the United States', 'Reviewed in the United States', 'Reviewed in the United States', 'Reviewed in the United States', 'Reviewed in the United States', 'Reviewed in the United States', 'Reviewed in the United States', 'Reviewed in the United States', 'Reviewed in the United States', 'Reviewed in the United States', 'Reviewed in the United States', 'Reviewed in the United States', 'Reviewed in the United States', 'Reviewed in the United States', 'Reviewed in the United States', 'Reviewed in the United States', 'Reviewed in the United States', 'Reviewed in the United States', 'Reviewed in the United States', 'Reviewed in the United States', 'Reviewed in the United States', 'Reviewed in the United States', 'Reviewed in the United States', 'Reviewed in the United States', 'Reviewed in the United States', 'Reviewed in the United States', 'Reviewed in the United States', 'Reviewed in the United States', 'Reviewed in the United States', 'Reviewed in the United States', 'Reviewed in the United States', 'Reviewed in the United States', 'Reviewed in the United States', 'Reviewed in the United States', 'Reviewed in the United States', 'Reviewed in the United States', 'Reviewed in the United States', 'Reviewed in the United States', 'Reviewed in the United States', 'Reviewed in the United States', 'Reviewed in the United States', 'Reviewed in the United States', 'Reviewed in the United States', 'Reviewed in the United States', 'Reviewed in the United States', 'Reviewed in the United States', 'Reviewed in the United States', 'Reviewed in the United States', 'Reviewed in the United States', 'Reviewed in the United States']
    ["I love books. Paper books. But, when traveling, they are not ideal. Aside from being heavy, they take up valuable luggage space. So, I broke down and bought my first Kindle. So far, I love it  I've read about 15 books on it in the first month ive used it.  Amazon gives you $5 to the Kindle store so I used that and all the other books I've gotten using my Libby pr Overdrive app.One of the main reasons I bought the Kindle I did is because I wanted library access. The only complaint is that I have to sign in every time to load a book to the Kindle. I use a VPN, so I get a text from Amazon to verify my log in. This is a bit obnoxious, but only take ls a few seconds.I read every night and the self-adjusting light is excellent. I also bought a case and I highly recommend getting one when you order your Kindle.The issues I've run into are:1.  The touch screen isn't as sensitive as a phone. So, you may have to tap a few times to get where you want to go.2.  Since the first charge, my Kindle will only get to 98% and no higher. I wait to charge until I'm less than 30%, usually much lower. Not sure if this is a common issue.3.  Wifi with a password at a hotel did not work. The Kindle would not open the password/sign on page. This was a hassle for a week as I had to tether to my phone hot spot every time I wanted to download or return a book.Overall, I am super happy with my first Kindle. I still love a paper book, but this is so much easier to travel with and swap books based on mood.", 'Warning: this will be a long review.  First, I\'ve owned Kindle e-readers since the Kindle keyboard.  I love to read.  I love to re-read my books - isn\'t that why we buy a device to haul all of our books around?  No more second suitcase for vacations, or bookbags to bring with my purse?  When my Kindle Voyage started to die, I started researching the new Kindles.  The biggest draw to the Oasis for me was the larger storage capapbilities.  No more having "too many books" for my Kindle to hold.  The second draw was the battery life- it was one of my favorite things about the Voyage.  My battery would last a week with it (yes, I read a LOT - sometimes my Kindle is on upwards of 15 hours a day).  So, imagine my disappointment when my new Oasis battery lasted 36 hours.  Ok,  I get it - I was downloading books and collections.  It takes a lot of battery.  But I am not so new to Kindle that I didn\'t already have the screen turned down and airplane mode on when not downloading.  It didn\'t matter - 36 hours.  After doing 2 factory resets with the aid of Kindle support (come on, I just want to read my books, not continuously reset my device and have to re-download everything), they finally decided the best thing to do was to send me a new one.  Maybe my first was a fluke..  No.  36 hours.  Amazon offered to replace it again.  I said no - if the battery is supposed to last 3 weeks (what I was told by the rep) and I read a lot, it should still be lasting a week!  So with the help of Jessica H (this girl is a gem - you guys need to give her a raise!), the downloaded my "logs" to the tech team.  When the tech team couldn\'t figure anything out, they had me manually download the logs and email them in.  Then I did a factory reset.  Then they had me let my Oasis completely deplete, wait for 2 minutes before plugging it in and recharging it, and then logging the battery constantly for the next 24+ hours.  Oh - but in the meantime the techs came back with the brilliant reasoning that the reason my battery wasn\'t lasting was that I had TOO MANY books downloaded to my device!  WTH?!  I had just gotten it and done factory restarts on it - there are less than 200 books on there!  And wait - wasn\'t that the whole point to having 32 GB of memory - so I COULD have my books on my device????  At the end of the call back, the only option they had for me was to once again replace a $260 device that had already failed TWICE.  Why?  Because my original purchase was 70 days ago, so I was beyond the return period.  Luckily Jessica H (seriously - wonderful, helpful, and always called when she said she would) spent THREE HOURS to get an exception to allow the return.  I will go out of Amazon and buy a replacement battery for my Voyage.  If I replace my Voyage again, it will be with a basic $99 Kindle - because I know what to expect from that - and not have high hopes that I had with the Oasis.', "Outstanding experience other than battery life, which is at best 1/3 of my paperwhite for actual usable reading time.  Love having the page turn buttons which was primary reason for getting the oasis. Slightly uncomfortable to hold 1-handed, but able to adjust & like the ability to switch hands & have screen auto-rotate.However, for trips, looks like I'll stick with the old Paperwhite. Paperwhite I can take on trip for a week, read heavily the entire trip, and come back with 50% power.  Oasis is dead after 3 days of heavy reading. Using both with wireless off, and at very low brightness.  On plus side Oasis does charge its itty bitty battery much faster, so if you don't mind being tethered to keeping an extra charger along, it is basically like another phone to charge every other day or so of heavy use.", 'The functionality usability readability etc are all excellent. This is my 4th kindle and I jumped once I saw another model with physical buttons to touch to turn pages. In my opinion going away from that option is the biggest downfall in kindle design after they removed it post “keyboard” editions.The battery life however is abysmal. Even legacy models were, as advertised, good for weeks between charges, and that was with reading on it on a more than average basis. This Oasis with warm light however is dead inside three days with minimal use. For example, I charged it two days ago so I can read before bed. I read that night, again when I woke up in the middle of the night for a bit, same last night, and it has already died on me on the third night. I don’t use a very high backlight so it shouldn’t be draining this fast.The older paper white I had did this and a call to customer service and an update solved the battery drain but amazon has gotten so global it no longer values customer service. If I can get a person on the phone to try to troubleshoot this oasis they barely speak English and if they do are rude and dismissive and I have been disconnected each time before they tried to fix the problem.Fix what you have amazon, before trying to add more services only one or two areas have access to, or using us to underwrite more terrible amazon tv shows. You are close to losing a customer.', 'Easy to set up.  Like the Bluetooth connectivity.  Easy to download and unload books using Kindle Unlimited.  The device is comfortable to hold and is lightweight.  I do like the setting capability for warm/bright white.  You will need the Wifi connection to get definitions of word, likewise to download books.  Have not used audible books as yet.  Compared to white light Kindle battery life may be somewhat shorter but it is okay for me.The browser is actually useless.  Too sensitive to enlarge screen and to interact with internet source.  Like when connecting at free wi-fi sites.  Screen display for browser is very poor.  (It is not the same as the reading screen for books downloaded).  Hopefully Amazon will have a software update.', 'I have had a Kindle Paperwhite for quite a few years.  Doing more reading in the dark, I thought it time to try spending the money on the current generation Oasis (for more uniform illumination and the warm light feature).  After owning it, I do also find I like the lighter weight and the balance of having more mass around the edge with the buttons.  My first ever e-reader was a non-touch Kobo...in which you held it at the bottom and scrolled through with a D-pad.  Having two buttons on the side seems more natural as a page turn.After setting up my Oasis, I started seeing two bright spots.  I contacted Amazon and there were not many questions until they issued me a replacement.  It was sent immediately, and it\'s holding up (I haven\'t had this level of service with Amazon before).There are a few aspects about the reader that people may be critical of.  The first is that it\'s meant for the Amazon echo-system.  For the Kindle books that you\'ve bought/acquired....those are easy to sync to your new device (and keep in their collections).  I\'ve used Caliber for converting other downloaded eBooks to Kindle format.  I\'ve found I\'ve had to manually upload them and then add them to collections once in the Kindle (trying to copy from "documents" from the old Kindle to new didn\'t work so well).The second aspect is battery life.  I like having the Kindle illuminated, which I know draws more power.  It does seem as though battery life is less than my old Paperwhite, but I don\'t have issues with charging more frequently.  I also haven\'t thrown out my old USB cables and power adapters, so I don\'t have as much grievance with this reader having micro-USB instead of USB C.The third is the interface for disabling the screen if all you want to use is the buttons (which I like, so that I can clean the screen of any flecks and not accidentally brush it and then pages are advanced).  You have to be in a book before going to the menu, tapping the ... button, then you have the option for turning off the screen.  That in itself isn\'t too hard....but then it stays like that until you put the Kindle to sleep.  Then, once you wake it up again, the touchscreen is now active.  I\'d prefer a way to set touchscreen as being inactive permanently....and then perhaps over-riding by an action with the buttons (like, for example, pressing either button for a set period of time).', "Buttons, I have been missing them, but the Oasis really is so far from perfect. I like to read with one hand, so buttons on the side, or back would be so much better. My Voyager was the right size to fit in a back pocket, this one is too wide for that. It's a good size for reading, and the screen is excellent. I really like the orange backlight for reading in a dark room.Make a kindle that is a little thicker than the oasis, same size screen, all plastic (less slippery than the Oasis), with physical buttons on the sides (both sides!) or back, orange backlight, and you'll have the perfect ebook reader.  Buttons on just one side, and the back would be acceptable if the screen rotates like the Oasis.", 'Love it. With as fast as I swap out tech my kindle PW3 was the only thing I kept and used constantly. This year I finally decided to upgrade my beloved kindle to the new oasis 3.I couldn’t be happier. The new oasis has a fantastic screen. Battery life has been excellent. I love the physical buttons. And the build quality is outstanding.It is my hope it holds up as well as my previous kindle PW3 and will serve me many years. I paired it with the leather case. Not the premium version just the standard and the fit and finish are amazing in hand. So far so good.I highly recommend this kindle. Especially if your coming from a much older model. It may not be much of a upgrade for those who have last years model but for me it was a huge leap forward.', 'I am a long time kindle user and have had several. My most recent is the 1st Oasis and I loved it. My main problem with it was with the charging cover. I didn’t like that it came off so easily and over time, it stopped switching from the cover to the main battery automatically so I had to remove it to keep reading. I liked that it made the oasis flat so I kept it on until I had to recharge.After reading about this new version having an amber light I decided to upgrade. Plus it’s waterproof and I read in the tub a lot. The screen is evenly lit, the warmer light is wonderful, the interface is fast, and its overall great.That being said, the size difference was a lot more noticeable than I expected. It’s very large. At least as big as my old paper white which I always felt was bulky. It seems unwieldy after using the Oasis 1 for the last few years. One of the things I loved about the oasis was the portable size that fit so well in my hand, purse, or jacket pocket. I will keep this and use it, but the second they come out with one similar in size to the original, with the bells and whistles this has, and with a seamless ergonomic case, I’m trading this bad boy in.', "As an old fart, an instruction and operations manual would be great. Also a trouble shooting guide would be wonderful. I had to return my first unit after spending 50 minutes with a very nice Amazon helper. She and I both agreed I needed a new one. Well, I hot the new one and had a lot of similar issues, but the issue is knowing how to use it. Now, after about 40 books, I've almost figured out how to use the damn thing. But I  read for 3 to 5 hours a night as part of my sleeping routine. I don't sleep well. I also use blue light glasses to cut the blue light hitting my eyes. My cell phone has this as an additional feature. Well, I've read a lot of books, all action/adventure, and I'm not sleeping any worse, but not a lot better. I think my problem is subject matter. I live in south Florida, have spent years in the Bahamas and Keys, and this is the backdrop to all of my books. So, I will now start searching of non-action/adventure style books. Might end up reading the Bible, but it's action/adventure most of the time on an even larger format.  So who knows??", 'There are better, less expensive products out there for reading.', 'This was my first Kindle purchase. Didn’t know what to expect. I’d used the app before but an actual Kindle doesn’t really compare. Took me a while to choose the right one and although the price for the Oasis is significantly higher, the two features that sold me were the page turn buttons (although I switched their functions) and the warm light. I was unaware of the e-ink technology but find it pleasing. It did take me a minute to get used to the flashing sometimes but now I understand it’s not a defect but rather a feature of the technology. I also stupidly thought the image on the screen when I opened the box was a sticker and spent a few seconds trying to peel it off. Learned that the technology doesn’t require any battery power to keep an image on the screen once the e-ink has drawn it. Nifty. I had resisted going electronic with books for years but what finally did it for me was a chunk of hair that was hidden and mashed in between some pages of a book I ordered off Amazon. I promptly threw the book away, continued reading it on the app on my iPad and began looking at Kindles. I’m glad I did. I love the Oasis. Special mention for the battery life. It lasts for weeks, especially if you turn on airplane mode when you don’t need the extra features.', 'Because of all the features it SAID it offered, and to not contribute to the destruction of more of our forests.My new  device is  defective,  does not work as advertised, which is actually fraud under WA Law.  Am battling Amazon for fair price of return of the device.1.  The tool bar does not respond to touch.2.  My device will not work with my private wifi network, nor...3.  will it "go back" from a page or return to "home when tapped.4. It sticks on certain pages, and must restart Kindle.5. The battery life is much less than advertised/promoted.I  did not try to set up the Oasis until Oct. 23rd. which was past the 30 day return. because I was out of WA state.I have spent 1 week of hours with 10 people to figure out problem, 2 of which promised a 100% return.  I called to set up the UPS return, the agent in South Africa, said I would receive only only 80% return b/c of restocking fee, or because under warranty, would exchange for a REFURBISHED ONE.  Interesting that they already have ones  they had to refurbish...I was so excited:  my first e-reader! Foolish me, I did not read complaints  b/c I pre-ordered  Shame on Bezos.  I recommend everyone read the Technology Edition of The Atlantic Monthly on Jeff Bezos and Amazon.', "WHY WAS MY $300+ KINDLE OASIS DELIVERED IN A PLASTIC BAG?!? A THREE HUNDRED DOLLAR KINDLE OASIS DELIVERED IN A CHEAPO WHITE PLASTIC BAG!I DON'T CARE IF IT CAME FROM THE DISTRIBUTION CENTER IN MY TOWN.I'VE BOUGHT UNDERWEAR FROM YOU GUYS THAT WAS PACKED SAFER!YOU SHOW DISRESPECT FOR YOUR CUSTOMERS HARD EARNED MONEY BY PLAYING ON-THE-CHEAP WITH SHIPPING FOR HIGHER-END PRODUCTS.* I will be editing this post, with a review of the actual Kindle Oasis, in a few days.", 'I love reading, and I’ve missed having buttons since I upgraded from a kindle keyboard to a paper white 7 years ago.  I’m ambidextrous so it’s great that you can hold in either hand.  I’m in to alternative medicine, and I think blue light causes my migraines.  I wear blue light blocking glasses at work and have my iPhone set to change to warm light at 6 pm.  As I go to bed reading every night, I believe the warm light has decreased my migraines and helped me sleep better.  I’m disappointed that I had to charge it after 2 weeks, but hoping it was just new use and that it will last longer on this charge.  I also reversed the page turn buttons, I thought it was weird to have to use the top button to turn forward.  If this had not been an option, I probably would have returned the kindle oasis and gotten a new paper white.', "ANOTHER UPDATE:I contacted customer service again this time through chat after rechecking the device warranty page.  It does in fact come with a 1 year warranty and Amazon is sending a free replacement.  I still don't like the fact that the screen cracked but at least Amazon addressed the issue.UPDATE:I've had the kindle since Nov 2019.  I was happy with it.  One of the selling points of an ereader is the ability to read outdoors and this model in particular is waterproof.  The first time I used the e-reader for a few hours in the hot sun it got so hot I could no longer use it.  I placed it in my tote that only had a towel in it.  When I went to read it later, the screen was cracked.  It wasn't dropped, it wasn't banged up.  Just cracked.  As mentioned below I have many other Kindles and have used them for years.  Carried in backpacks, suitcases etc.  Never a problem.  I've read in more recent reviews that this model has a problem with screen cracking.  I would agree.  When I contacted customer service they said since I was outside of the 3 month warranty (not a year?) there was nothing they could do except offer me 15% off a new one.  No options for repair at all.DO NOT BUY THE KINDLE OASIS until a new version with a better screen is available.Finally the e-reader I've been looking for.  I own a non-Kindle brand, a Kindle Touch and an older model Kindle Paperwhite.  This has my favorite features of each of those plus more.  I love the option of buttons for page turning and touch mode, I no longer have to worry about gloves or lotions getting in the way.  I can flip easily from between reading left and right sided reading, making drinking coffee and reading easy.  The waterproofing means poolside reading isn't a worry.  Plus my new favorite feature, amber reading at bedtime.  All this plus the ease of using Amazon's Kindle features and benefits.  I'm happy with battery life, as with my other Kindles I keep it in airplane mode unless downloading books.", 'The Oasis is very nice, but I prefer the Kindle Keyboard 3G, Free 3G + Wi-Fi, 6" E Ink Display model. AMAZON, will you EVER bring this model back? Please?(My Kindle Keyboard 3G, Free 3G + Wi-Fi, 6" E Ink Display was 9+ years old - I dropped it [from only 1-1/2-feet high] on a ceramic tile floor and the screen broke. The screen is now permanently 1/3 screen saver whether on/off.  It fit in  my purse and/or pocket perfectly and had buttons for left or right handed page turning. It was simple and PERFECT and more like a REAL book)The Oasis is just too big and I do not like the lighting or the touch screen - at all. The touch screen to far too sensitive - constantly losing/searching for my page. The blanket or the dog\'s whiskers barely touch the edge of the screen and the pages are turning.  The auto page rotation drives me nuts. The unit feels \'slippery\' - there\'s no texture to it at all - it\'s hard to hold onto.The leather case (which is 1/2 plastic) doesn\'t help much - it\'s flimsy and cheap - definitely not worth $50.00The Kindle Fire was a total waste of money.There\'s a lot of Bells & Whistles on the Oasis, which is great if you like Bells & Whistles (why I give it 4-stars), but I prefer to keep it simple with a unit like the Kindle Keyboard 3G, Free 3G + Wi-Fi, 6" E Ink Display model - it was closer to reading a REAL book.', 'I really love the concept of this kindle.  I love the warm light and button features which maybe justifies the cost, initially.  The warm light it especially a boon if you share a bed with someone who falls asleep before you.  The light it very customizable so as not to bother your eyes or people near you.  The ergonomic design and buttons are another benefit of the Oasis.  I purchased a case because the metal of the kindle is cold.  I do wish the backing was the same as traditional Kindle, the soft rubber stuff, but it’s a personal preference.The Oasis is almost completely wonderful.  But, for the money, the battery life is a major reading buzz kill.  My old Kindle 4 had weeks of battery life.  Weeks!  This has a few days at best.  Don’t expect long battery life if you’re a voracious reader.  Expect to plan charging frequently.  You can experiment with light settings and WiFi settings to see if it helps your battery life but I’ve not found significant differences.', 'This my third e-reader. The previous one was a 7th-gen Kindle. That was good, but the screen was too small, the backlighting inadequate, the pages too slow to turn, and I didn’t like swiping. All these features are fixed in the Oasis. The buttons turn pages instantly, the screen lighting is perfect, and the screen is the minimum I like for extended reading. It’s lightweight. It’s great!And it has the standard Kindle long-storage battery and high resolution.I look forward to a further version that is closer in size to a paperback book, but will happily use this until then.', 'I like the new kindle oasis because of the backlighting (means I can read while my husband sleeps).  However, the battery life is just over two days if you delete the wi-fi info.  If you have the wi-fi data input, you cannot turn it off and on so then the battery lasts only about a day and a half.  Using airplane mode does not extend the battery much.  Really disappointing since I read for about two to six hours a day.  So that means at the most, the battery lasts 12 hours without recharging.  Again, really disappointed with the battery.  My first kindle battery lasted a month (without wi-fi on).', 'I replaced my Voyage with the new Oasis.  The ability to choose a warm background for the text is a game changer.  I loved my Voyage, it has traveled the world with me, but really like my Oasis.  I have seen several write of very short battery life and at first I thought I was seeing that also.  Then I realized it was downloading my library, as I had instructed, in the background.  Once that was done it seems to have battery life equivalent to what I saw with my Voyage.  So far I have few complaints.  My next Kindle ereader  i think I will order ad free.Amazon has gotten more aggressive with their advertising and I am a bit put off by it.After using the Oasis for a few months I decided to amend my review.  It is too big.  It won’t find in jacket pockets, Jean pockets or anything I normally wear.  I cannot take it with me as I have always done with my Voyage.  I still carry my Voyage, the Oasis stays home.  It is more like a hard back book, not really good for travel. Perhaps a nice Paperwhite would be a better choice.  The Oasis stays on the nightstand.', 'This is an outstanding kindle. The screen is easy on the eyes. I purchased the gold color for myself and the graphite as a gift. I love that you have the option of turning the pages with the up (forward) or down ((backward) buttons. You also have the choice of touching the bottom of screen on left or right side of screen for turning pages forward or backwards. To get to menus just swipe.across top of screen. I haven’t owned device long enough to comment on battery life. The only complaint I have is the ergonomic grip. I’m not a fan of the ergonomic grip but I found the remedy for this by purchasing a case that conceals the bulky grip by placing Kindle inside the plastic holder in back of cover that has a smooth flat back. I purchased 32 GB without ads and with WiFi. I didn’t see any advantage in spending extra $50 for free cellular when all you get is free Wikipedia and the Amazon store data on the cellular. With a cell phone with unlimited data, I didn’t see the benefit in spending the extra money.', 'I have had many versions of the Kindle, and this is my second Oasis. They have been more than satisfactory, as is this one, but it does have a couple of quirks. If you read more than two hours a day, even if you are careful and only use the internet as briefly as possible and do not exceed the mid lightness position, a week to ten days is the max on a charge; certainly adequate but not "weeks." Due to the variation in thickness, if the device is placed on a flat surface to read, best change pages by tapping the screen, not pressing the buttons. Using the buttons will rock the device and provide an uncertain result. If holding it in the hands to read do not hold it by or have a finger on the black area to the left of the reading area. Otherwise a small inadvertent squeeze on the black area on the right will send you to what seems to be a random location earlier in the copy or article you are reading. And while not a drawback, I have been unable to figure out the purpose of "warming" the screen. My lack of imagination, no doubt.', 'I’d hesitated to buy this because it’s expensive. I loved my Paperwhite and Fire, and thought, “How much better could the Oasis be, really”?It is THAT much better! Virtually perfect, as far as I can see!', "I am thrilled with this Oasis! I thought long and hard before buying this and read a million reviews before deciding to go for it, many of which made me nervous. So many people have said that it's overpriced for what it is or that it feels flimsy, but in my opinion, it is well worth what I paid for it. For those that complain about the micro-usb for recharging instead of the usb-c connector, who cares? lol As long as it charges, I don't care what kind of cable it needs. I have congenital cataracts and I'm prone to migraines, both of which make me sensitive to cool bright white light, so the warm light option with the ability to dim the light as needed on the new Oasis was an absolute must. I love to read and relax in the tub so the waterproof aspect of this Kindle was very important. I bought the blue water-safe cover that Amazon makes for it as well. It's such a relief to no longer fear dropping my device in the water accidentally, although I have no plans to actually test whether it actually is waterproof, lol.  Holding it is a dream - it's not heavy at all but is a perfect weight (and it does not feel flimsy!), and the way the back is shaped lets it rest easily in one hand. The page forward and page back buttons are awesome -  I always hated having to swipe pages to turn them on other devices. I can switch hands easily as the screen rotates automatically. I have checked out ebooks from my local library and bought some Kindle books as well, and all of them loaded to my Kindle with no issues. I'm using Amazon's payment plan to pay for it, which is amazing, so I didn't have to pay for it all at once. I have absolutely no regrets about buying this device!", "I have nothing bad to say about this product - there are a fair number of negative reviews but I have not experienced anything negative. My previous Kindle was from 2014 (I believe) so it had no backlighting, was much thicker, the touchscreen was more faulty and less fast, there were no buttons, etc. This new one is fast, the touchscreen works great, and I loooooove the ability to customize the backlighting (brightness and warmth). I also really like that the screen flips so you can pass it to your right/left hand. A few other features I like are the ability to turn off the touchscreen (so you don't have to worry about it when you're in the groove of reading), and the ability to see the book cover vs. list of books in your library. I am 150% satisfied with this purchase and would highly recommend to anyone.", "the first thing you realize is it's half or a third shorter than the old Kindle I had. Then there's the fact it's in black and white - which shouldn't mean much except on my Iphone the kindle app does show colors. But really, then you get right down to it, it's a luxury item when people are starving and worse in these times so these are far from anything other than embarrassing little comments and really, I should be thankful and I am that on this Memorial Day 2020 here in time and place where the future is unwritten and uncertain, I have a relatively modern convenience in my hand - that can hold more books that I can read and provide me the convenience to read 24/7.  Yes, if you're reading this and I work with you, even on work books I've purchased and in fact, sadly or valiantly, I have quite a few of those! Stay safe. Heed science. Appreciate technology.", 'I bought the new kindle oasis to take the place of my perfectly fine paper white. I just thought I deserved the top of the line kindle with all the reading I do. I am Not at all impressed with the battery life of this new kindle oasis. I get about 3 days of reading in before I have to recharge it. That is with WiFi turned off, brightness set at 7 and reading for roughly 3 hours a night. After spending $297.00 after tax, I am very very disappointed in this device. I thought about contacting Amazon for a replacement, but they replace your brand new devices with refurbished ones. I don’t think that’s cool since it’s less than a month old. Until the battery drain issue is resolved, I would not recommend purchasing this.I do love the design and the build. It’s unfortunate it doesn’t come remotely close to what the specs says it will do before charging....', "I use this mainly for reading library books. Its hard to navigate to the books I've downloaded. Pretty sure this is done by design so you will pay Amazon for book downloads. I tried the free trial of Kindle Unlimited and most of the books I wanted to read still had to be paid for. It doesn't appear to download Epub books either.I ordered this because I thought it was supposed to have blue light filtering, I guess it does but I really can't tell the difference. I also thought this would have a deeper black and white contrast for reading at night but when I switch to the black screen its really more of a gray screen and still very bright.Even at the largest text size I still need reading glasses at night with this (I use the the 1.5x drugstore reading glasses) though I can read with no problem during the day.At the end of the day a regular tablet would have been more versatile and I wouldn't have to check out books from my phone to push them to the Kindle.", "I was hesitant to upgrade from my 3rd generation kindle keyboard because of the lack of a keyboard but I LOVE this kindle. The touchscreen makes the keyboard unnecessary and the backlight feature is wonderful. I did want the side buttons which is why I chose this version. You can flip it over to use the buttons on either side depending on how you are holding it.  Or you can tap the screen to advance the page. But the combination of all those features for me make it the perfect upgrade and I don't regret it at all. Battery life seems fine to me, usually about two weeks with me reading a little every day. Seems to charge pretty quickly as well. Highly recommend especially for those with the older kindle.", "This is my very first e-reader. I wasn't sure which one I would go with but after doing my own research I decided on the Kindle Oasis for the bigger screen, the extra LEDS, and the page turning buttons. I love reading but its getting harder for me to do because of my eyes not being as good as they used to be. I get migraines frequently and when I try to read conventional books, the extra eye strain makes those migraines worse and/or come about more often. It's also getting harder to hold books for longer periods of time due to joint pains in my hands so instead of putting my books away for good, I decided to try an E-Reader. I ordered this product and it came about 2 days later, so shipping was fast and reliable. Everything came in perfect working order and it was easy to set up. I am already a Prime member so everything I needed to get started getting my paper book collection in ebook form was just a few clicks away. The customization on the brightness level is great. I can read in low to no light or bright light with no problem. Font sizes can be changed for me to see the words easier and bookmarking where I've left off is a breeze. I am really loving this e-reader and wish I had gotten it much sooner. I would 100% recommend this product to anyone with similar problems as me, or anyone for that matter who loves to read as it is so portable and easy to take all my books wherever I go.", 'Battery life is okay at best and I think the battery meter is unreliable sometimes.  The screen saver is an eyesore.  It grows ugly and tedious after a while.  I opted for no ads because the ads were even worse so the extra twenty dollars was worth it to me.The most frustrating thing though is that sometimes when I tap the screen to advance the page in a book it randomly jumps to a place near the beginning of the book.  Occasionally tapping "Back" on the top menu will return my to  the proper location, but not always and then it doesn\'t remember my place in the book.', "I was looking for a waterproof e-reader to replace my Barnes and Noble Nook that frequently overheats outdoors, thereby rendering it unusable just when I want to ready most at the pool or on the patio.. I also found that I was constantly touching the wrong spots on the Nook screen and closing my books accidentally. The design of the Kindle Oasis is easier to hold without accidentally turning pages or returning to the home screen. I love the option to use the buttons to turn the pages. It makes it easier to manage with just one hand. I also find it much easier to check out books from my local library on the Kindle. So far, the book hasn't overheated outside. Fortunately, I haven't had to test the waterproof capabilities. The warm light is nice for bedtime reading. So far, so good. The only criticism I have is that it does not come with a charger you can plug into the wall. I was able to find one that works, but for the price, this item should include its own charger.", "I loved my old Kindle, but it was slow and kinda unconfirmed to hold for long periods of time. Not the case with the new 2019 Oasis. This thing is super responsive to touch and rotation. I actually use the hardware buttons more than I expected for turning pages, just because they're right where my thumb is resting naturally. The little bump in the back feels more like holding a folded book. I take this to the gym every day and read for a couple hours while I'm jogging on the treadmill - helps keep me going, as I always want to finish just one more chapter, which results in extra exercise and better commitment to my fitness goals.", 'I was an early adopter of the Kindle and have owned several.  Once the iPad Pros came out, I switched to reading on the iPad with the Kindle app.  Since I always read/work using Dark Mode on my Macs and iPads, when I saw that the Kindle Oasis had a warm light I decided to give it a try.  I like the warm light on the Oasis, it definitely helps reduce eye strain.  The main negatives are the sluggish speed due to an under powered processor and the dark mode is too dark and does not provide enough contrast.  Hopefully, Amazon will address both of these issues in future versions.  I would also very much like to see Kindle be able to connect to Dropbox directly (which is a feature in the new Kobos).', "I chose the Oasis over the Paperwhite because it is large enough to make me feel like I'm reading a book and I have room to make the print as comfortably large as I want without adding numerous page turns. Speaking of page turns, the turn button is so convenient and ensures that I don't leap ahead or back unintentionally. Being able to set the brightness of the screen, the warmth of the background, the size of the type, and being able to flip it open (I got the leather cover too) in the middle of the night and read without turning on a light is so convenient.The ability to access word definitions, Wikipedia, and more right from my reading screen are wonderful and it's light weight means I can take it with me easily and I always have a book with me!Some people have complained about the battery life. My Oasis has days' long battery storage and recharges quickly.I'm very pleased with my choice and would do it again.", "This is the fourth Kindle I've owned.  My first was a DX purchased in 2009; the second was a Touch purchased in 2011, my third was a gift of a Voyage in 2015 and finally my Oasis.  I've been interesting in book readers since I read about the possibility of their production in an editorial in a science fiction magazine in the 80s.  The selling point was the ability to change the size of the text for the elderly and the visual impaired.  Amazon has done a fabulous job with this as well as the ease of reading on their Kindles.  I got the Touch so my dad could use the DX.  I liked the Touch because it was lighter than the DX however it wasn't backlit which I thought was a great improvement when I saw a backlit Nook.  The DX got to heavy for my dad so I gave him my Touch and my husband gave me the Voyage which I was happy with the back lighting however I didn't care for how it adjusted the lighting so I turned that feature off.  I got my husband an Oasis in 2017 when the DX got too heavy for him and he loved it so much that he bought one for his brother-in-law to use when he was recovering from hip surgery.  The buttons on my Voyage started to act flaky in mid 2019 so a put an Oasis on my wishlist.  My only hesitation is it looked like it was designed for right handed people.  I thought it was so cool when I got mine and the screen flips so you can hold it and use the buttons left handed.  I decided to try the new adaptable lighting and so far it is a major improvement to what was on my Voyage.", "I really like the size of the Oasis, it's light and easy to handle.  The flexibility of use is phenomenal!  You can flip it to use the buttons on the left or right, or you can touch the screen on the left or right, or you can swipe.  Setting the font to a size you're comfortable with is simple.  I've had no problems reading in the bright light of day or the darkness of evening.  The battery goes and goes and goes.  It came with three months of Kindle Unlimited and I will definitely be continuing the subscription when that runs out. It is terrific to be able to read the same book on my Kindle or my phone or my tablet and have the app keep track of where I'm at, even if I'm listening to the audio book in my car and wanting to switch back to reading at home.  The waterproof feature is neat but I haven't had occasion to try that out yet, maybe next summer at the beach.  It was a little pricey but so far it seems to be worth it.", 'First things first: don’t buy this under Amazon’s trade-in program. Although Amazon states that you’ll get 20% off on a new kindle, that’s a lie. I was not given 20% off this brick, I was given 20% off an Echo. If I had known that the ad for 20% wasn’t going to be toward a new kindle, I would have kept my old Paperwhite.  Despite going back and forth with Amazon and pointing out that the website clearly states it’s off the kindle...well, their response was basically “sorry, nope, we lie.”Secondly, I love ebooks. I’ve purchased hundreds. As much as I’d love to keep doing that, this thing won’t connect to the WiFi in my home. No other device has a problem connecting. Amazon’s chatbot is as helpful as Roy from The IT Crowd in resolving the issue.Anyway, Kobo’s Libra does everything this can do for $100 less. I’ll be returning this brick and buying one of those.', "The only issue I have is you can't immersion read... You can't listen to audiobooks while also reading. I really miss that feature since I got use to it on the kindle app on mobile.  I also feel for the price your pay for the Oasis it should definitely be a feature that's why 4 stars instead of 5. I am hoping at some point kindle will upgrade this feature  I have had the kindle fire but the kindle Oasis is definitely a better option for the avid reader . I enjoy that it doesn't let you do much else but read. That way I won't get distracted by web browser and game play or apps. It's like carrying a million books in one hand. It really holds alot. I get constantly ask what the device is and people are always impressed with it . I like sleek and light weight feel.", 'Absolutely love the warm light with this kindle! My eyes are dry and I have trouble seeing even with glasses. I keep my phone and laptop on dark or warm mode, and when I saw this kindle had warm mode I knew I had to have it! The warm mode is very nice and soothing to my eyes. I don’t even feel like I’m reading on a screen. My old kindle paperwhite I’ve had for almost 8 years and I just decided it was time for a new one. I also love that I can use the Libby app on my phone, check out ebooks from my local library, and send them directly to my kindle. I also enjoy the buttons and that the screen flips depending on how I want to hold it. The battery life has been amazing and so far I’ve already read several books on a single charge. I haven’t tested the water resistance yet and hopefully I won’t have to. Overall very pleased with my purchase and have no complaints as of right now.', 'I debated about getting a kindle for quite a while. I thought I would miss the feel of a regular book. Now that I have a Kindle Oasis I absolutely love it. It has so many great features. Not only does it have a built in dictionary but it has a feature called X-ray that lets you look up characters in the book and get information about them. There are also so many other nice features. I was also pleasantly surprised to learn that most of the books I want to read are available in ebook format from my local library through an app called Overdrive. It’s so convenient no more trips to the library to get and return books. I tried a free three month subscription to Kindle unlimited but I’m not going to continue it. As I said I can get most of the book I want to read through my library plus if I do want to purchase an ebook they are very inexpensive.I chose an Oasis after doing a lot of research and I’m very glad I did. It’s was worth the increase in price over the paper white.', 'The Kindle Oasis, which I received a few days ago is such a disappointment. My Kindle Fire stopped connecting to the internet and since I need that to order new books, I decided to "upgrade". NOT. The Oasis is a step down, not particularly user friendly, and a waste of money. Why make changes that don\'t need to be done. Silk is OK, scrolling with my fire was much better than tuning pages, why put buttons on the Oasis when a touch on the screen will do the job. I read a lot and often have 2 books going.I read the user manual and have a book on Oasis, but I find I get on an old Paperwhite to do much of my reading and reading several things on the internet. Live and learn. My first disappointment with Amazon.', "First of all, I really love this Kindle.  The Oasis is everything is claims to be with one exception.  The screen brightness can be turned down (I like it at 0 since I do not like to read with a back lit display) and the temperature (color) is a wonderful feature.  It makes it feel more like a real book.The ONE area where I am disappointed is the the battery life.  All things considered, the battery life is good.  I can probably get through two novels on one charge, but from what I had read, I expected a week of battery life, not two days.  I read one novel on a full battery charge which took me about 8 hours.  I turned off the screen when I stopped (I have two kids, so I get interrupted a lot) and had the brightness almost all the way down most of the time.  When I was done with the book, I had 51% battery life left.  Like I said, this is not bad, but not quite what I had expected.Overall, I am really enjoying it.  I'm happy I got it and happy I paid extra for the larger memory option and making it ad-free.", 'original NEW Oasis had issues when i had it just for one month - with freezing when attempting to open a downloaded book, 2nd replacement was a refurbished edition - returned that, then replacement of a NEW Oasis arrived - this one made it 4 days before problems -  adjustable light constantly changed, (yes, you can set the light you want it to be at - but this model changed the light all the time),  then the whole screen went a black/grey color, and decided that Oasis is not for me.  did like the size, weight and style of the Oasis - but none of that makes up for the lack of being able to use it.', "I received the 10th gen Kindle Oasis today. And just like my 9th gen Kindle Oasis I can't update the software. The option to check for an update is grayed out. Meaning you can no longer request it you just have to wait till they do it. I don't know when 5.13.1 was released but I use my 9th gen every single day and check every single day for the update which it won't allow me to do and both the old device that is 3 years old shows 5.12.3 with no options upgrade either device. I've contacted customer support who was of no help basically telling me that I can manually update the device I just received today or return it within 30 days. Why would anyone this day and age with over the air updates for all devices including refrigerators want to pay $260 plus dollars for something that had outdated software on it with no option but to manually sit down at a computer and do it yourself. I recently purchased a boox poke 2 and I'm waiting on the shipment. I'm very excited because so far it seems superior in many ways and will allow me to read my Kindle library which at this point I would gladly abandon.", "Do the people who create new Kindle versions actually read books on them?1. Biggest problem:  I am 73 and a voracious reader.  My fingers and hands also have some arthritis.  It is hard to hold this new Kindle Oasis because there are no places to hold it without unwittingly touching the screen and thus turning the page.  The Oasis does have one Side with the page turning buttons which makes easier to hold on the right side.  Thus I don't understand why a side can't be bigger on the left.  THE COVERS AVAILABLE DO NOT ADDRESS THIS PROBLEM.2. Second problem:Sorting Feature-  I have over a thousand books on the device or in the cloud.  I like Collections, but they are not easy to retrieve.  I have to page through 70 pages to get to Woods, Stuart.  Especially when trying to add books to a collection3. Third problem: Receiving books I have ordered months earlier.  Today, I knew I should have JD Robb's newest IN Death.  However it was not on my home screen like before, when books would be delivered seamlessly.  When I went to Recent -Unread, it still wasn't there.  I had to go to the store.  Look it up.  It told me I had purchased it today, but I had to download it from the store page.I SICERELY HOPE SOMEONE WITH AUTHORITY READS THIS AND DOES SOMETHING TO MAKE THE KINDLE BETTER.", 'Your browser does not support HTML5 video.\n\n\n  \xa0I\'ve been a long term kindle user, but never a kindle owner. I personally LOVE books, especially physical ones I can feel, flip, store. But I enjoy nighttime reading, and the light from an electronic is less intrusive (and easier when traveling!!) So when the opportunity came to possess my very own kindle, I was ecstatic.  It is everything I always wanted! It is lightweight, durable, easy to use, and has a stupidly long battery life!I have seen multiple comments about the fact this "updated" kindle uses an outdated charging source, but I don\'t personally see the fuss. It charges well overnight, and honestly unless you are reading every day, 9+ hours a day you won\'t really notice anything.I personally LOVE the page turning button, and the fact you can switch which button does what. AND that no matter which way you flip your kindle, the top button still functions as a top button. (Read one of the other reviews, a delightful woman goes into this feature more with a video!)If you are looking to buy a kindle, I highly recommend this one. And I agree witb others, if you\'re already splurging,  go in for the 32 not the 8. You\'ll thank us later.', "I really love this Kindle device in that it's light weight with a long lasting battery as long as you don't have the backlit screen cranked all the way up. On a setting of 25% ~ 33% the battery should last several weeks easy. I really like the design but a case is an absolute must because it's far better and more comfortable to hold and it won't let you scratch you device. I purchased my with 32 gigs of storage and personally anything less than 32 gigs is a shame because once you start reading on this beautiful device you'll be wanting to purchase a bunch more books.", 'I struggled to decide if I wanted to cough up the extra money for this e-reader, but I am so glad I did!  A few of the things I like about it are the 7" screen, the even and adjustable lighting, and the push button or screen tap features. However, the best feature, over my previous Paperwhite, is the fast speed of the processor.  I would never think the processor speed would make the reading experience much different, but it sure does. The battery life is as described.  I have only had it a week and have been through about 2.5 books (1 of which was an Audible book) and have only recharged it once when it went down to 30%. I love this thing!']
    


```python


dic = { "user":all_users, "rating":all_ratings, "date":all_dates, "region":all_regions, "review":all_reviews }
dat = pd.DataFrame(dic, columns=['user','rating','date','region','review'])

dat.to_csv("20210621_kindle_reviews.csv", index=False, encoding="utf-8")
dat
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>user</th>
      <th>rating</th>
      <th>date</th>
      <th>region</th>
      <th>review</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Worldwidehavok</td>
      <td>4</td>
      <td>April 25, 2021</td>
      <td>Reviewed in the United States</td>
      <td>I love books. Paper books. But, when traveling...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>JackandCyn1</td>
      <td>2</td>
      <td>August 29, 2020</td>
      <td>Reviewed in the United States</td>
      <td>Warning: this will be a long review.  First, I...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Dave_5k</td>
      <td>3</td>
      <td>October 21, 2020</td>
      <td>Reviewed in the United States</td>
      <td>Outstanding experience other than battery life...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>CWM</td>
      <td>3</td>
      <td>June 17, 2020</td>
      <td>Reviewed in the United States</td>
      <td>The functionality usability readability etc ar...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Zippy1643</td>
      <td>4</td>
      <td>October 10, 2019</td>
      <td>Reviewed in the United States</td>
      <td>Easy to set up.  Like the Bluetooth connectivi...</td>
    </tr>
    <tr>
      <th>5</th>
      <td>David Rosenberg</td>
      <td>5</td>
      <td>August 26, 2020</td>
      <td>Reviewed in the United States</td>
      <td>I have had a Kindle Paperwhite for quite a few...</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Dave C</td>
      <td>3</td>
      <td>January 14, 2020</td>
      <td>Reviewed in the United States</td>
      <td>Buttons, I have been missing them, but the Oas...</td>
    </tr>
    <tr>
      <th>7</th>
      <td>J. Reyes</td>
      <td>5</td>
      <td>October 20, 2019</td>
      <td>Reviewed in the United States</td>
      <td>Love it. With as fast as I swap out tech my ki...</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Heather O</td>
      <td>4</td>
      <td>June 22, 2020</td>
      <td>Reviewed in the United States</td>
      <td>I am a long time kindle user and have had seve...</td>
    </tr>
    <tr>
      <th>9</th>
      <td>James R. Van der Veen</td>
      <td>5</td>
      <td>February 22, 2021</td>
      <td>Reviewed in the United States</td>
      <td>As an old fart, an instruction and operations ...</td>
    </tr>
    <tr>
      <th>10</th>
      <td>frank</td>
      <td>1</td>
      <td>August 14, 2019</td>
      <td>Reviewed in the United States</td>
      <td>There are better, less expensive products out ...</td>
    </tr>
    <tr>
      <th>11</th>
      <td>AO</td>
      <td>5</td>
      <td>March 24, 2020</td>
      <td>Reviewed in the United States</td>
      <td>This was my first Kindle purchase. Didn’t know...</td>
    </tr>
    <tr>
      <th>12</th>
      <td>M.L. Powers, MS</td>
      <td>2</td>
      <td>October 26, 2019</td>
      <td>Reviewed in the United States</td>
      <td>Because of all the features it SAID it offered...</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Susan</td>
      <td>1</td>
      <td>December 12, 2020</td>
      <td>Reviewed in the United States</td>
      <td>WHY WAS MY $300+ KINDLE OASIS DELIVERED IN A P...</td>
    </tr>
    <tr>
      <th>14</th>
      <td>astateprincess</td>
      <td>5</td>
      <td>August 21, 2019</td>
      <td>Reviewed in the United States</td>
      <td>I love reading, and I’ve missed having buttons...</td>
    </tr>
    <tr>
      <th>15</th>
      <td>LN</td>
      <td>3</td>
      <td>January 4, 2020</td>
      <td>Reviewed in the United States</td>
      <td>ANOTHER UPDATE:I contacted customer service ag...</td>
    </tr>
    <tr>
      <th>16</th>
      <td>L.A. Blu</td>
      <td>4</td>
      <td>January 2, 2020</td>
      <td>Reviewed in the United States</td>
      <td>The Oasis is very nice, but I prefer the Kindl...</td>
    </tr>
    <tr>
      <th>17</th>
      <td>dontpanic42</td>
      <td>4</td>
      <td>January 11, 2021</td>
      <td>Reviewed in the United States</td>
      <td>I really love the concept of this kindle.  I l...</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Kindle Customer</td>
      <td>5</td>
      <td>March 25, 2021</td>
      <td>Reviewed in the United States</td>
      <td>This my third e-reader. The previous one was a...</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Kaniki</td>
      <td>3</td>
      <td>June 4, 2021</td>
      <td>Reviewed in the United States</td>
      <td>I like the new kindle oasis because of the bac...</td>
    </tr>
    <tr>
      <th>20</th>
      <td>Ronald L. Babb</td>
      <td>4</td>
      <td>December 26, 2019</td>
      <td>Reviewed in the United States</td>
      <td>I replaced my Voyage with the new Oasis.  The ...</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Beauty Star</td>
      <td>5</td>
      <td>October 20, 2020</td>
      <td>Reviewed in the United States</td>
      <td>This is an outstanding kindle. The screen is e...</td>
    </tr>
    <tr>
      <th>22</th>
      <td>Edson W. Kempe</td>
      <td>4</td>
      <td>August 23, 2020</td>
      <td>Reviewed in the United States</td>
      <td>I have had many versions of the Kindle, and th...</td>
    </tr>
    <tr>
      <th>23</th>
      <td>M. lewis</td>
      <td>5</td>
      <td>March 29, 2020</td>
      <td>Reviewed in the United States</td>
      <td>I’d hesitated to buy this because it’s expensi...</td>
    </tr>
    <tr>
      <th>24</th>
      <td>Jules T.</td>
      <td>5</td>
      <td>January 6, 2020</td>
      <td>Reviewed in the United States</td>
      <td>I am thrilled with this Oasis! I thought long ...</td>
    </tr>
    <tr>
      <th>25</th>
      <td>thisismaggie</td>
      <td>5</td>
      <td>October 12, 2019</td>
      <td>Reviewed in the United States</td>
      <td>I have nothing bad to say about this product -...</td>
    </tr>
    <tr>
      <th>26</th>
      <td>Zike</td>
      <td>3</td>
      <td>May 25, 2020</td>
      <td>Reviewed in the United States</td>
      <td>the first thing you realize is it's half or a ...</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Rmill</td>
      <td>2</td>
      <td>December 5, 2019</td>
      <td>Reviewed in the United States</td>
      <td>I bought the new kindle oasis to take the plac...</td>
    </tr>
    <tr>
      <th>28</th>
      <td>cristin</td>
      <td>2</td>
      <td>January 3, 2021</td>
      <td>Reviewed in the United States</td>
      <td>I use this mainly for reading library books. I...</td>
    </tr>
    <tr>
      <th>29</th>
      <td>Cindy Duncan</td>
      <td>5</td>
      <td>December 11, 2019</td>
      <td>Reviewed in the United States</td>
      <td>I was hesitant to upgrade from my 3rd generati...</td>
    </tr>
    <tr>
      <th>30</th>
      <td>Tabitha Smith</td>
      <td>5</td>
      <td>April 5, 2021</td>
      <td>Reviewed in the United States</td>
      <td>This is my very first e-reader. I wasn't sure ...</td>
    </tr>
    <tr>
      <th>31</th>
      <td>Kindle Customer</td>
      <td>3</td>
      <td>November 28, 2020</td>
      <td>Reviewed in the United States</td>
      <td>Battery life is okay at best and I think the b...</td>
    </tr>
    <tr>
      <th>32</th>
      <td>LGS625</td>
      <td>4</td>
      <td>August 5, 2019</td>
      <td>Reviewed in the United States</td>
      <td>I was looking for a waterproof e-reader to rep...</td>
    </tr>
    <tr>
      <th>33</th>
      <td>Kep</td>
      <td>5</td>
      <td>August 10, 2019</td>
      <td>Reviewed in the United States</td>
      <td>I loved my old Kindle, but it was slow and kin...</td>
    </tr>
    <tr>
      <th>34</th>
      <td>Chris R. Johnson</td>
      <td>4</td>
      <td>April 20, 2021</td>
      <td>Reviewed in the United States</td>
      <td>I was an early adopter of the Kindle and have ...</td>
    </tr>
    <tr>
      <th>35</th>
      <td>Ginny L.</td>
      <td>5</td>
      <td>April 27, 2021</td>
      <td>Reviewed in the United States</td>
      <td>I chose the Oasis over the Paperwhite because ...</td>
    </tr>
    <tr>
      <th>36</th>
      <td>Cynthia Miller</td>
      <td>5</td>
      <td>January 28, 2020</td>
      <td>Reviewed in the United States</td>
      <td>This is the fourth Kindle I've owned.  My firs...</td>
    </tr>
    <tr>
      <th>37</th>
      <td>Contrisger</td>
      <td>5</td>
      <td>January 28, 2020</td>
      <td>Reviewed in the United States</td>
      <td>I really like the size of the Oasis, it's ligh...</td>
    </tr>
    <tr>
      <th>38</th>
      <td>Marcos Yturri</td>
      <td>1</td>
      <td>April 1, 2021</td>
      <td>Reviewed in the United States</td>
      <td>First things first: don’t buy this under Amazo...</td>
    </tr>
    <tr>
      <th>39</th>
      <td>Alisha T</td>
      <td>4</td>
      <td>June 21, 2020</td>
      <td>Reviewed in the United States</td>
      <td>The only issue I have is you can't immersion r...</td>
    </tr>
    <tr>
      <th>40</th>
      <td>Erin Nicole Hollingsworth</td>
      <td>5</td>
      <td>October 22, 2020</td>
      <td>Reviewed in the United States</td>
      <td>Absolutely love the warm light with this kindl...</td>
    </tr>
    <tr>
      <th>41</th>
      <td>Will</td>
      <td>5</td>
      <td>January 5, 2021</td>
      <td>Reviewed in the United States</td>
      <td>I debated about getting a kindle for quite a w...</td>
    </tr>
    <tr>
      <th>42</th>
      <td>Kindle Customer</td>
      <td>1</td>
      <td>March 25, 2021</td>
      <td>Reviewed in the United States</td>
      <td>The Kindle Oasis, which I received a few days ...</td>
    </tr>
    <tr>
      <th>43</th>
      <td>Linda Napoli</td>
      <td>4</td>
      <td>September 28, 2020</td>
      <td>Reviewed in the United States</td>
      <td>First of all, I really love this Kindle.  The ...</td>
    </tr>
    <tr>
      <th>44</th>
      <td>ila b</td>
      <td>1</td>
      <td>January 25, 2021</td>
      <td>Reviewed in the United States</td>
      <td>original NEW Oasis had issues when i had it ju...</td>
    </tr>
    <tr>
      <th>45</th>
      <td>Bret</td>
      <td>1</td>
      <td>July 17, 2020</td>
      <td>Reviewed in the United States</td>
      <td>I received the 10th gen Kindle Oasis today. An...</td>
    </tr>
    <tr>
      <th>46</th>
      <td>VERONICA</td>
      <td>3</td>
      <td>February 4, 2020</td>
      <td>Reviewed in the United States</td>
      <td>Do the people who create new Kindle versions a...</td>
    </tr>
    <tr>
      <th>47</th>
      <td>Kirsten</td>
      <td>5</td>
      <td>December 27, 2020</td>
      <td>Reviewed in the United States</td>
      <td>Your browser does not support HTML5 video.\n\n...</td>
    </tr>
    <tr>
      <th>48</th>
      <td>Douglas Meyer</td>
      <td>5</td>
      <td>August 28, 2019</td>
      <td>Reviewed in the United States</td>
      <td>I really love this Kindle device in that it's ...</td>
    </tr>
    <tr>
      <th>49</th>
      <td>John J. Floro</td>
      <td>5</td>
      <td>January 18, 2021</td>
      <td>Reviewed in the United States</td>
      <td>I struggled to decide if I wanted to cough up ...</td>
    </tr>
  </tbody>
</table>
</div>




```python

```