# HealthTag for HackTheBurgh 2019

## Inspiration
We all like travelling and we often find ourselves in places where we don't speak the language.
What if we have an emergency, how do we communicate our details to the doctors and emergency teams?
We created Health Tag to help communicate the medical record in a situation where there is a language barrier or the user has a speech impediment problem. But Health Tag is for everyone, it's the fastest way to communicate all the important information with the medical staff.

## What it does
Health Tag is an NFC tag that holds your medical record and basic information. When you are in an emergency room the staff can just tap the tag with their phone and they will have access to all your information:
- Blood type
- Allergies
- Medications
- Pathologies
- Vaccinations
- Emergency contact details
- Languages you speak

Health tag comes as a simple web app with a scanning page, a user page, and a new tag page only accessible to doctors.

The use of web interfaces allow for the platform to be run on any device that has an NFC antenna: this should facilitate medical staff to adopt our system.

Privacy concern? The data is all encrypted. And only authorized users can read and write new tags.

## How we built it
We built Health Tag with Flask and MongoDB.
We also based our code on web-nfc for the NFC interface.
The app is hosted on Google Cloud Platform.

## Challenges we ran into
We got entangled with redirecting and sending http request quite often.
It was challenging to get the REST api to provide a safe way to comunicate the data without making easily interceptable.

Frontend is very frustrating. Getting the styles right was very time consuming.

But most importantly overcoming badly documented APIs! (We got stuck on integrating Flask with GCP)

## Accomplishments that we're proud of
We are proud of our teamwork, we managed to quickly set up the git workflow so we didn't encounter any major issue, and we split the task decently so there were no overlaps.

We are proud that the overall app works all around and that we achieved all the basic features that we planned to implement.

All of the above especially because Jack is at his first hackathon (wohoo) and Eleonora at her second!!

## What we learned
**Lessons**
- Badly documented APIs are a waste of time (sometimes).
- Frontend is pain.

**Technologies**
We were all fairly new to the technologies we used. It was very interesting to learn web-nfc APIs.
We were also quite unfamiliar with MongoDB and Flask so that was fun to play around with.
Some of us are also new to Javascript.

## What's next for HealthTag
The very first next-step is to allow different languages in the UI.
We need to make the tag blend with your clothing items, whether it's a bracelet, a neckless or a watch strap.
We also need to work on the admin panel to allow medics to edit the record of the patient.

