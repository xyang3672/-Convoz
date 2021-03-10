import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from datetime import datetime
import json

#TODO: Finalize the user data to be sent in the email.
#data is a dictionary
def sent_email(data):
    today = datetime.now()
    date = today.strftime("%d/%m/%Y %H:%M:%S")
    message = MIMEMultipart()
    message["Subject"] = "Summary of Your Meeting"
    message["From"] = "zoombullies338@gmail.com" #create your own email to send
    message["To"] = data['email'] #email that you are sending to
    #Adjust html to how you want it to look like
    html = """\
    <html>    
<<<<<<< HEAD
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
       <a href="https://google.com" class="button">Go to Webpage</a>
=======
    <h1 style="text-align: center">Today's Meeting</h1>
    <hr>
    <h2 style ="text-align: left;">For meeting <span style="color:#A53FD2; font-weight: normal">{0}</span> on
    <span style="color:#A53FD2; font-weight: normal">{1}</span></h2>
    <hr>
    <h2 style ="color:black; text-align: left">Number of Offenses: {2}  </h2>
    <h2 style ="color:black; text-align: left"> Top Offenses: </h2>
    <h3 style ="color:#E37100; text-align: left; padding-left: 40px; font-weight: normal"> {3} </h3>
    <h3 style ="color:#E37100; text-align: left; padding-left: 40px; font-weight: normal"> {4} </h3>
    <h3 style ="color:#E37100; text-align: left; padding-left: 40px; font-weight: normal"> {5} </h3>
    <hr>
    <h2 style ="color:black; text-align: left"> What to focus on for next time: </h2>
    <h3 style ="color:#E37100; text-align: left; padding-left: 40px; font-weight: normal"> Create a feedback dependent on the data gathered from meeting</h3>
>>>>>>> e6200248f8fcb3641f4ab3fbf472a449a4944df4
    </html>
    """.format('Jun', date, data['count'], data['offenses'][0][0], data['offenses'][1][0],data['offenses'][2][0])

    part = MIMEText(html, "html")

    message.attach(part)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login("zoombullies338@gmail.com", "compsci21")
        server.sendmail(
<<<<<<< HEAD
            "zoombullies338@gmail.com", data[recipient]['email'], message.as_string()
        )
=======
            "zoombullies338@gmail.com", data['email'], message.as_string()
        )
>>>>>>> e6200248f8fcb3641f4ab3fbf472a449a4944df4
