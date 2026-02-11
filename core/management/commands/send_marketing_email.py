import os

from django.core.management.base import BaseCommand
from django.template.loader import render_to_string
from dotenv import load_dotenv

from core.utils import send_email

load_dotenv()

SALES_EMAIL = os.getenv("SALES_EMAIL")
COMMUNITY_EMAIL = os.getenv("COMMUNITY_EMAIL")

emails = [
    "didouh.1994@gmail.com",
    "mondayutibe88@gmail.com",
    "oluwatobioreniyi@gmail.com",
    "chukwuebukaanueyiagu@gmail.com",
    "uzoamakaudoh5@gmail.com",
    "dominichope77@gmail.com",
    "yahuzaspidey@gmail.com",
    "kipmooreeofficial@gmail.com",
    "midelstech@gmail.com",
    "dbriggs012@uniport.edu.ng",
    "dikedarleen@gmail.com",
    "musadanladi@trinasr.com",
    "belinda123frank@gmail.com",
    "gifted4good@gmail.com",
    "andresbriggs@gmail.com",
    "ibimdonbriggs21@gmail.com",
    "ngoziqueen60@gmail.com",
    "okunlolafz@gmail.com",
    "diepriyeominorisa@gmail.com",
    "ajakaiyetessy30@gmail.com",
    "dominionechefula@gmail.com",
    "amoni.ngofaka@gmail.com",
    "easyeghe@gmail.com",
    "magdalenegeorge719@gmail.com",
    "Henryin17@gmail.com",
    "amneshettima@gmail.com",
    "danielakinselure@gmail.com",
    "mg0578233@gmail.com",
    "andremuzzy98@gmail.com",
    "ilaibialambo@gmail.com",
    "adelaniadedeji@gmail.com",
    "humphreyukatejitpaul@gmail.com",
    "muonakakelvinc@gmail.com",
    "seozmikz@gmail.com",
    "gracylov12@gmail.com",
    "nwagwumichael@gmail.com",
    "pleasuresolace71@gmail.com",
    "ibinabobriggs.ib@gmail.com",
    "pereosaisai22@gmail.com",
    "enochprecious25@gmail.com",
    "davidinmichael@gmail.com",
    "davidmizzy731@gmail.com",
]

test_emails = [
    "davidinmichael@gmail.com",
    "davidmizzy731@gmail.com",
]

recipients = {
    "didouh.1994@gmail.com": "Ugonna Helen Nwachukwu",
    "mondayutibe88@gmail.com": "UTIBE MONDAY",
    "oluwatobioreniyi@gmail.com": "Oluwatobi A Oreniyi",
    "chukwuebukaanueyiagu@gmail.com": "Ebuka",
    "uzoamakaudoh5@gmail.com": "Uzoamaka Chinenyenwa Udoh",
    "dominichope77@gmail.com": "Ekongson Hope Dominic",
    "yahuzaspidey@gmail.com": "big spidey",
    "kipmooreeofficial@gmail.com": "Golden",
    "midelstech@gmail.com": "Favour Godwin",
    "dbriggs012@uniport.edu.ng": "Briggs Daye Lolo",
    "dikedarleen@gmail.com": "Dike, Amarachi Esther",
    "musadanladi@trinasr.com": "Musa Danladi Esq",
    "belinda123frank@gmail.com": "Belinda frank",
    "gifted4good@gmail.com": "Arc. Gift Wuche",
    "andresbriggs@gmail.com": "Belema Briggs lolo",
    "ibimdonbriggs21@gmail.com": "Ibim Don Briggs",
    "ngoziqueen60@gmail.com": "Bernard",
    "okunlolafz@gmail.com": "Okunlola Faozee",
    "diepriyeominorisa@gmail.com": "Diepriye Ominorisa",
    "ajakaiyetessy30@gmail.com": "Ajakaiye Tessy Blessing",
    "dominionechefula@gmail.com": "Echefulachukwu Dominion",
    "amoni.ngofaka@gmail.com": "Amoni Ngofaka Linda",
    "easyeghe@gmail.com": "Easy Eghe",
    "magdalenegeorge719@gmail.com": "Magdalene Tabo George",
    "Henryin17@gmail.com": "Henry Inyama",
    "amneshettima@gmail.com": "Amne",
    "danielakinselure@gmail.com": "Daniel Akinselure Daniel",
    "mg0578233@gmail.com": "Matthew Ehi Gift",
    "andremuzzy98@gmail.com": "Andrew Muzan",
    "ilaibialambo@gmail.com": "ILAIBI ALAMBO",
    "adelaniadedeji@gmail.com": "Deji Adelani",
    "humphreyukatejitpaul@gmail.com": "Humphrey ukatejit Paul",
    "muonakakelvinc@gmail.com": "Muonaka chukwuemeka",
    "seozmikz@gmail.com": "Siyeofori Michael",
    "gracylov12@gmail.com": "Chukwu Grace",
    "nwagwumichael@gmail.com": "Nwagwu Michael",
    "pleasuresolace71@gmail.com": "Pleasure Ordukwu",
    "ibinabobriggs.ib@gmail.com": "Ibinabo Briggs",
    "pereosaisai22@gmail.com": "Pere Osaisai",
    "enochprecious25@gmail.com": "Precious c Enoch",
    "jamilahakogaree@gmail.com": "Jamilaha Ahmad Kogari",
    "frankiebubah@gmail.com": "Franca Yellow",
    "Akhigbeblessed@gmail.com": "Blessed",
    "davidinmichael@gmail.com": "David Michael",
    "davidmizzy731@gmail.com": "David",
    "joyn53423@gmail.com": "Joy Nnamdi",
    "justkendice@gmail.com": "Ken-Adele Godswill",
    "empowermenty415@gmail.com": "Abdulazeez",
    "abdulazeezibrahim847@gmail.com": "Abdulazeez",
    "ezevivian2real@gmail.com": "Eze Vivian Nkiruka",
    "ogechukwu970@gmail.com": "Ogechukwu Cynthia Ukwuani",
    "easyeghe@gmail.com": "Easy Eghe",
    "temidayo190@hotmail.com": "Abiodun Emmanuel",
    "Ibinabobriggs.ib@gmail.com": "Ibinabo Briggs",
}

test_receipients = {
    "davidinmichael@gmail.com": "David Michael",
    "davidmizzy731@gmail.com": "David",
}


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        count = 0
        for email, name in recipients.items():
            count += 1
            context = {"name": name}
            template = render_to_string("core/marketing_email.html", context)

            send_email(
                email,
                "Thanks for Attending - How to Package & Sell Your Skills",
                template,
                COMMUNITY_EMAIL,
            )

            self.stdout.write(
                self.style.SUCCESS(f"{count}. Email sent to {name} <{email}>")
            )

        self.stdout.write(self.style.SUCCESS("All emails sent!"))
