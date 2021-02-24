import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

#TODO: Create another script to automate the process.
recipients = ["zoombullies338@gmail.com" #additional emails here as strings, separated by commas]

#TODO: Indiviualize emails to each participant depending on their meeting actions.
for recipient in recipients:
    message = MIMEMultipart()
    message["Subject"] = "Summary of Your Meeting"
    message["From"] = "zoombullies338@gmail.com"
    message["To"] = recipient
    html = """\
    <html>    
       <h1 style="text-align: center">Today's Meeting</h1>
       <hr>
       <h2 style ="text-align: left;">For meeting <span style="color:#A53FD2; font-weight: normal">{0}</span> on
       <span style="color:#A53FD2; font-weight: normal">{1}</span> at <span style="color:#A53FD2;font-weight: normal">
             {2}</span> </h2>
       <h2 style="text-align: left;"> Attendees: <span style="color:black; font-weight: normal">
          {3} </span></h2>
       <hr>
       <h2 style ="color:black; text-align: left"> {6} </h2>
       <h3 style ="color:#17B50E; text-align: left; padding-left: 40px; font-weight: normal"> {7} </h3>
       <h3 style ="color:#E37100; text-align: left; padding-left: 40px; font-weight: normal"> {8} </h3>
       <hr>
       <h2 style ="color:black; text-align: left"> What to focus on for next time: </h2>
       <h3 style ="color:black; text-align: left; font-weight: normal; padding-left: 40px;"> {4}</h3>
       <div id="test">
       </div>
       <script>
         fetch(scratch.json).then(response => response.json())
.then(data => { document.querySelector(#test).innerText = data.sentence})
       </script>
    </html>
    """.format("99999", "2-19-21", "8:46 PM", "Attendees here",
               " Equal distribution, Good job!", "filler", "Speaking Emotions:", "excited", "impolite")

    part = MIMEText(html, "html")

    message.attach(part)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login("zoombullies338@gmail.com", "compsci21")
        server.sendmail(
            "zoombullies338@gmail.com", recipient, message.as_string()
        )