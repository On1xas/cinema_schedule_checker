Пример запроса:

https://soft.silverscreen.by:8443/wssite/webapi/xml?mode=events&date=2021-06-23&eventId=1410&theater=2

### **Параметры запроса**:

<table>
   <tr>
    <th>Name</th>
    <th>Type</th>
    <th>Variants</th>
    <th>Discription</th>
   </tr>
   <tr>
    <td>mode</td>
    <td>обязательный</td>
    <td>events </td>
    <td>Список событий</td>
   </tr>
    <tr>
    <td></td>
    <td></td>  
    <td>showdates</td> 
    <td>Список Дат</td>  
    </tr>
    <tr>
    <td></td>
    <td></td>  
    <td>showtimes</td> 
    <td>Список времени сеансов</td>  
    </tr>
    <tr>
    <td>date</td>
    <td>необязательный</td>  
    <td></td> 
    <td>выборка по дате сеанса</td>  
    </tr>
 <tr>
    <td>eventid</td>
    <td>необязательный</td>  
    <td></td> 
    <td>выборка по id события</td>  
    </tr>
 <tr>
    <td>theater</td>
    <td>необязательный</td>  
    <td></td> 
    <td>отбор по объекту</td>  
    </tr>
 </table>

Номера кинотеатров для запроса theater:
<li>
2 - Arena City Silver Screen cinema\
<li>
3 - VOKA CINEMA by Silver Screen\
<li>
11 - mooon в ТРК Triniti\
<li>
19 - mooon в ТРЦ Palazzo


Дерево ответа об сеансе получаемого от API программного обеспечения букера:

            0 - <ID>180224</ID>
            1 - <dtAccounting/>
            2 - <dttmShowStart>2023-1-21T11:15:00</dttmShowStart>
            3 - <dttmShowStartUTC/>
            4 - <dttmShowEnd/>
            5 - <dttmShowEndUTC/>
            6 - <ShowSalesStartTime/>
            7 - <ShowSalesStartTimeUTC/>
            8 - <ShowSalesEndTime/>
            9 - <ShowSalesEndTimeUTC/>
           10 - <ShowReservationStartTime/>
           11 - <ShowReservationStartTimeUTC/>
           12 - <ShowReservationEndTime/>
           13 - <ShowReservationEndTimeUTC/>
           14 - <EventID>2643</EventID>
           15 - <Title><![CDATA[ Кот в сапогах 2: Последнее желание ]]></Title>
           16 - <OriginalTitle><![CDATA[ Кот в сапогах 2: Последнее желание]]></OriginalTitle>
           17 - <ProductionYear>2022</ProductionYear>
           18 - <LengthInMinutes>110</LengthInMinutes>
           19 - <dtLocalRelease>2023-1-14T00:00:00</dtLocalRelease>
           20 - <Rating>зрителям, достигшим 6 лет</Rating>
           21 - <RatingLabel>6+</RatingLabel>
           22 - <RatingImageUrl/>
           23 - <EventType/>
           24 - <Genres>комедия, мультфильм, приключения</Genres>
           25 - <TheatreID>2</TheatreID>
           26 - <TheatreAuditriumID>18</TheatreAuditriumID>
           27 - <TheatreAuditriumURL/>
           28 - <TheatreAuditorium>Зал 4</TheatreAuditorium>
           29 - <Theatre>Silver Screen в ТРЦ Arena city</Theatre>
           30 - <TheatreAndAuditorium>Silver Screen в ТРЦ Arena city, Зал 4</TheatreAndAuditorium>
           31 - <PresentationMethodAndLanguage/>
           32 - <EventSeries/>
           33 - <ShowURL>https://silverscreen.by/afisha/#times=kot-v-sapogah-2-poslednee-zhelanie-2643&showID=180224</ShowURL>
           34 - <PresentationMethod>2D</PresentationMethod>
           35 - <EventURL>https://silverscreen.by/afisha/kot-v-sapogah-2-poslednee-zhelanie-2643</EventURL>
           36 - <Images>
                <EventMicroImagePortrait/>
                <EventSmallImagePortrait/>
                <EventMediumImagePortrait/>
                <EventLargeImagePortrait>https://portal.silverscreen.by:8448/meadiaStorage/bin/system/cinema/eventsphoto/medium/10016.jpeg</EventLargeImagePortrait>
                </Images>
           37 - <ContentDescriptors/>
           38 - <hav_tickets>true</hav_tickets>
           39 - <min_price>7</min_price>
           40 - <max_price>32</max_price>