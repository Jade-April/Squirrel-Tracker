from django.db import models
from django.utils.translation import gettext as _
from django.core import validators

class Squirrel(models.Model):
    Latitude=models.DecimalField(
            max_digits=16, 
            decimal_places=13,
            validators=[
                        validators.MaxValueValidator(41),
                        validators.MinValueValidator(40),
                        ],
            help_text=_('Latitude coordinate for squirrel sighting point'),
            )

    Longitude=models.DecimalField(
            max_digits=16,   
            decimal_places=13,
            validators=[
                        validators.MaxValueValidator(-73),
                        validators.MinValueValidator(-74),
                        ],
            help_text=_('Longitude coordinate for squirrel sighting point'),
            )

    Unique_Squirrel_ID=models.CharField(
            unique=True,
            max_length=20,
            validators=[validators.RegexValidator("\d{1,2}[A-I]-[PA]M-\d{4}-\d{2}",message='Please enter the right ID.')],
            help_text=_('Identification tag for each squirrel sightings. The tag is comprised of "Hectare ID" + "Shift" + "Date" + "Hectare Squirrel Number.'),
            )

    PM='PM'
    AM='AM'
    shift_choices=(
        (PM,'P.M.'),
        (AM,'A.M.'),
        )
    Shift=models.CharField(
        max_length=2,
        choices=shift_choices,
        help_text=_('Value is either "AM" or "PM," to communicate whether or not the sighting session occurred in the morning or late afternoon.'),
        )
    
    Date=models.DateField(
            help_text=_('Concatenation of the sighting session day,month and year.(formate: YYYY-MM-DD)'),
        )
    
    ADULT='Adult'
    JUVENILE='Juvenile'
    age_choices=(
        (ADULT,'adult'),
        (JUVENILE,'juvenile'),
        )
    Age=models.CharField(
        max_length=10,
        choices=age_choices,
        help_text=_('Value is either "adult" or "juvenile".'),
        blank=True,
        )
    
    GRAY='Gray'
    CINNAMON='Cinnamon'
    BLACK='Black'
    fur_choices=(
        (GRAY,'gray'),
        (CINNAMON,'cinnamon'),
        (BLACK,'black'),
        )
    Primary_Fur_Color=models.CharField(
        max_length=10,
        choices=fur_choices,
        help_text=_('Value is either "gray," "cinnamon" or "black".'),
        blank=True,
        )
    
    GROUND_PLANE='Ground Plane'
    ABOVE_GROUND='Above Ground'
    location_choices=(
            (GROUND_PLANE,'ground plane'),
            (ABOVE_GROUND,'above ground'),
            )
    Location=models.CharField(
            max_length=20,
            choices=location_choices,
            help_text=_('Value is either "ground plane" or "above ground." Sighters were instructed to indicate the location of where the squirrel was when first sighted.'),
            blank=True,
            )

    Specific_Location=models.CharField(
            max_length=100,
            help_text=_('Sighters occasionally added commentary on the squirrel location. These notes are provided here.'),
            blank=True,
            )

    Running=models.BooleanField(
            help_text=_('Squirrel was seen running.'),
            )

    Chasing=models.BooleanField(
            help_text=_('Squirrel was seen chasing another squirrel.'),
            )

    Climbing=models.BooleanField(
            help_text=_('Squirrel was seen climbing a tree or other environmental landmark.'),
            )

    Eating=models.BooleanField(
            help_text=_('Squirrel was seen eating.'),
            )

    Foraging=models.BooleanField(
            help_text=_('Squirrel was seen foraging for food.'),
            )

    Other_Activities=models.CharField(
            max_length=100,
            blank=True,
            )

    Kuks=models.BooleanField(
            help_text=_('Squirrel was heard kukking, a chirpy vocal communication used for a variety of reasons.'),
            )

    Quaas=models.BooleanField(
            help_text=_('Squirrel was heard quaaing, an elongated vocal communication which can indicate the presence of a ground predator such as a dog.'),
            )

    Moans=models.BooleanField(
            help_text=_('Squirrel was heard moaning, a high-pitched vocal communication which can indicate the presence of an air predator such as a hawk.'),
            )
    Tail_flags=models.BooleanField(
            help_text=_("Squirrel was seen flagging its tail. Flagging is a whipping motion used to exaggerate squirrel's size and confuse rivals or predators. Looks as if the squirrel is scribbling with tail into the air.")
            )

    Tail_twitches=models.BooleanField(
            help_text=_('Squirrel was seen twitching its tail. Looks like a wave running through the tail, like a breakdancer doing the arm wave. Often used to communicate interest, curiosity.'),
            )

    Approaches=models.BooleanField(
            help_text=_('Squirrel was seen approaching human, seeking food.'),
            )

    Indifferent=models.BooleanField(
            help_text=_('Squirrel was indifferent to human presence.'),
            )

    Runs_from=models.BooleanField(
            help_text=_('Squirrel was seen running from humans, seeing them as a threat.'),
            )

    def __str__(self):
        return self.Unique_Squirrel_ID

# Create your models here.
