from django import forms
from django.contrib.auth.models import User
from users.models import Payment, Address
from django.contrib.auth.forms import UserCreationForm
from creditcards.forms import CardNumberField, CardExpiryField, SecurityCodeField


from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.utils.translation import ugettext as _
from django.utils.translation import pgettext_lazy
from django.utils import timezone



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    


    class Meta: #namespace for configurations for user models
        model = User
        fields = ['username', 'email','first_name', 'last_name','password1', 'password2']

class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


def validate_ccnumber (value):
    if not value.isdigit():
        raise ValidationError(_('%(value)s is not a valid card number.'), params={'value':value},)
    else:
        return value

def validate_cccode (value):
    if not value.isdigit():
        raise ValidationError(_('%(value)s is not a valid CVV/CVC number.'), params={'value':value},)
    else:
        return value

def validate_ccexpiry(value):
    if value < timezone.now().date():
        raise ValidationError("This card has expired.")
        

class PaymentForm(forms.ModelForm):
    #cc_number = CardNumberField(label='Card Number')
    #cc_expiry = CardExpiryField(label='Expiration Date')
    #cc_code = SecurityCodeField(label='CVV/CVC')

    cc_number = forms.CharField(max_length = 20, min_length = 15, validators=[validate_ccnumber], label = 'Credit Card Number', required = False)
    cc_expiry = forms.DateField(input_formats=['%m/%y', '%m/%Y'], help_text = "Please use the following format: <em>MM/YY</em>.", label = 'Card Expiration Date' , required = False, validators= [validate_ccexpiry])
    cc_code = forms.CharField(max_length = 3, min_length = 3, help_text = "Please use the following format: <em>CVV or CVC</em>.", validators=[validate_cccode], label = 'CVV/CVC', required = False)


    class Meta:
        model = Payment
        model.user = User
        fields = ['cc_number', 'cc_expiry','cc_code']

#class PaymentForm2(forms.ModelForm):
 #   cc_number = forms.IntegerField(max_length = 20, min_length = 16, validators=[])
  #  cc_expiry = forms.DateField(input_formats='%m/%y%', help_text = "Please use the following format: <em>MM/YY</em>.")
   # cc_code = forms.IntegerField(max_length = 3, min_length = 3, help_text = "Please use the following format: <em>CVV or CVC</em>.")



def validate_zipcode (value):
    if not value.isdigit():
        raise ValidationError(_('%(value)s is not a valid zip code number.'), params={'value':value},)
    else:
        return value

COUNTRIES = (
    ('US', _('United States')),
    ('AF', _('Afghanistan')), 
    ('AX', _('Aland Islands')), 
    ('AL', _('Albania')), 
    ('DZ', _('Algeria')), 
    ('AS', _('American Samoa')), 
    ('AD', _('Andorra')), 
    ('AO', _('Angola')), 
    ('AI', _('Anguilla')), 
    ('AQ', _('Antarctica')), 
    ('AG', _('Antigua and Barbuda')), 
    ('AR', _('Argentina')), 
    ('AM', _('Armenia')), 
    ('AW', _('Aruba')), 
    ('AU', _('Australia')), 
    ('AT', _('Austria')), 
    ('AZ', _('Azerbaijan')), 
    ('BS', _('Bahamas')), 
    ('BH', _('Bahrain')), 
    ('BD', _('Bangladesh')), 
    ('BB', _('Barbados')), 
    ('BY', _('Belarus')), 
    ('BE', _('Belgium')), 
    ('BZ', _('Belize')), 
    ('BJ', _('Benin')), 
    ('BM', _('Bermuda')), 
    ('BT', _('Bhutan')), 
    ('BO', _('Bolivia')), 
    ('BA', _('Bosnia and Herzegovina')), 
    ('BW', _('Botswana')), 
    ('BV', _('Bouvet Island')), 
    ('BR', _('Brazil')), 
    ('IO', _('British Indian Ocean Territory')), 
    ('BN', _('Brunei Darussalam')), 
    ('BG', _('Bulgaria')), 
    ('BF', _('Burkina Faso')), 
    ('BI', _('Burundi')), 
    ('KH', _('Cambodia')), 
    ('CM', _('Cameroon')), 
    ('CA', _('Canada')), 
    ('CV', _('Cape Verde')), 
    ('KY', _('Cayman Islands')), 
    ('CF', _('Central African Republic')), 
    ('TD', _('Chad')), 
    ('CL', _('Chile')), 
    ('CN', _('China')), 
    ('CX', _('Christmas Island')), 
    ('CC', _('Cocos (Keeling) Islands')), 
    ('CO', _('Colombia')), 
    ('KM', _('Comoros')), 
    ('CG', _('Congo')), 
    ('CD', _('Congo, The Democratic Republic of the')), 
    ('CK', _('Cook Islands')), 
    ('CR', _('Costa Rica')), 
    ('CI', _('Cote d\'Ivoire')), 
    ('HR', _('Croatia')), 
    ('CU', _('Cuba')), 
    ('CY', _('Cyprus')), 
    ('CZ', _('Czech Republic')), 
    ('DK', _('Denmark')), 
    ('DJ', _('Djibouti')), 
    ('DM', _('Dominica')), 
    ('DO', _('Dominican Republic')), 
    ('EC', _('Ecuador')), 
    ('EG', _('Egypt')), 
    ('SV', _('El Salvador')), 
    ('GQ', _('Equatorial Guinea')), 
    ('ER', _('Eritrea')), 
    ('EE', _('Estonia')), 
    ('ET', _('Ethiopia')), 
    ('FK', _('Falkland Islands (Malvinas)')), 
    ('FO', _('Faroe Islands')), 
    ('FJ', _('Fiji')), 
    ('FI', _('Finland')), 
    ('FR', _('France')), 
    ('GF', _('French Guiana')), 
    ('PF', _('French Polynesia')), 
    ('TF', _('French Southern Territories')), 
    ('GA', _('Gabon')), 
    ('GM', _('Gambia')), 
    ('GE', _('Georgia')), 
    ('DE', _('Germany')), 
    ('GH', _('Ghana')), 
    ('GI', _('Gibraltar')), 
    ('GR', _('Greece')), 
    ('GL', _('Greenland')), 
    ('GD', _('Grenada')), 
    ('GP', _('Guadeloupe')), 
    ('GU', _('Guam')), 
    ('GT', _('Guatemala')), 
    ('GG', _('Guernsey')), 
    ('GN', _('Guinea')), 
    ('GW', _('Guinea-Bissau')), 
    ('GY', _('Guyana')), 
    ('HT', _('Haiti')), 
    ('HM', _('Heard Island and McDonald Islands')), 
    ('VA', _('Holy See (Vatican City State)')), 
    ('HN', _('Honduras')), 
    ('HK', _('Hong Kong')), 
    ('HU', _('Hungary')), 
    ('IS', _('Iceland')), 
    ('IN', _('India')), 
    ('ID', _('Indonesia')), 
    ('IR', _('Iran, Islamic Republic of')), 
    ('IQ', _('Iraq')), 
    ('IE', _('Ireland')), 
    ('IM', _('Isle of Man')), 
    ('IL', _('Israel')), 
    ('IT', _('Italy')), 
    ('JM', _('Jamaica')), 
    ('JP', _('Japan')), 
    ('JE', _('Jersey')), 
    ('JO', _('Jordan')), 
    ('KZ', _('Kazakhstan')), 
    ('KE', _('Kenya')), 
    ('KI', _('Kiribati')), 
    ('KP', _('Korea, Democratic People\'s Republic of')), 
    ('KR', _('Korea, Republic of')), 
    ('KW', _('Kuwait')), 
    ('KG', _('Kyrgyzstan')), 
    ('LA', _('Lao People\'s Democratic Republic')), 
    ('LV', _('Latvia')), 
    ('LB', _('Lebanon')), 
    ('LS', _('Lesotho')), 
    ('LR', _('Liberia')), 
    ('LY', _('Libyan Arab Jamahiriya')), 
    ('LI', _('Liechtenstein')), 
    ('LT', _('Lithuania')), 
    ('LU', _('Luxembourg')), 
    ('MO', _('Macao')), 
    ('MK', _('Macedonia, The Former Yugoslav Republic of')), 
    ('MG', _('Madagascar')), 
    ('MW', _('Malawi')), 
    ('MY', _('Malaysia')), 
    ('MV', _('Maldives')), 
    ('ML', _('Mali')), 
    ('MT', _('Malta')), 
    ('MH', _('Marshall Islands')), 
    ('MQ', _('Martinique')), 
    ('MR', _('Mauritania')), 
    ('MU', _('Mauritius')), 
    ('YT', _('Mayotte')), 
    ('MX', _('Mexico')), 
    ('FM', _('Micronesia, Federated States of')), 
    ('MD', _('Moldova')), 
    ('MC', _('Monaco')), 
    ('MN', _('Mongolia')), 
    ('ME', _('Montenegro')), 
    ('MS', _('Montserrat')), 
    ('MA', _('Morocco')), 
    ('MZ', _('Mozambique')), 
    ('MM', _('Myanmar')), 
    ('NA', _('Namibia')), 
    ('NR', _('Nauru')), 
    ('NP', _('Nepal')), 
    ('NL', _('Netherlands')), 
    ('AN', _('Netherlands Antilles')), 
    ('NC', _('New Caledonia')), 
    ('NZ', _('New Zealand')), 
    ('NI', _('Nicaragua')), 
    ('NE', _('Niger')), 
    ('NG', _('Nigeria')), 
    ('NU', _('Niue')), 
    ('NF', _('Norfolk Island')), 
    ('MP', _('Northern Mariana Islands')), 
    ('NO', _('Norway')), 
    ('OM', _('Oman')), 
    ('PK', _('Pakistan')), 
    ('PW', _('Palau')), 
    ('PS', _('Palestinian Territory, Occupied')), 
    ('PA', _('Panama')), 
    ('PG', _('Papua New Guinea')), 
    ('PY', _('Paraguay')), 
    ('PE', _('Peru')), 
    ('PH', _('Philippines')), 
    ('PN', _('Pitcairn')), 
    ('PL', _('Poland')), 
    ('PT', _('Portugal')), 
    ('PR', _('Puerto Rico')), 
    ('QA', _('Qatar')), 
    ('RE', _('Reunion')), 
    ('RO', _('Romania')), 
    ('RU', _('Russian Federation')), 
    ('RW', _('Rwanda')), 
    ('BL', _('Saint Barthelemy')), 
    ('SH', _('Saint Helena')), 
    ('KN', _('Saint Kitts and Nevis')), 
    ('LC', _('Saint Lucia')), 
    ('MF', _('Saint Martin')), 
    ('PM', _('Saint Pierre and Miquelon')), 
    ('VC', _('Saint Vincent and the Grenadines')), 
    ('WS', _('Samoa')), 
    ('SM', _('San Marino')), 
    ('ST', _('Sao Tome and Principe')), 
    ('SA', _('Saudi Arabia')), 
    ('SN', _('Senegal')), 
    ('RS', _('Serbia')), 
    ('SC', _('Seychelles')), 
    ('SL', _('Sierra Leone')), 
    ('SG', _('Singapore')), 
    ('SK', _('Slovakia')), 
    ('SI', _('Slovenia')), 
    ('SB', _('Solomon Islands')), 
    ('SO', _('Somalia')), 
    ('ZA', _('South Africa')), 
    ('GS', _('South Georgia and the South Sandwich Islands')), 
    ('ES', _('Spain')), 
    ('LK', _('Sri Lanka')), 
    ('SD', _('Sudan')), 
    ('SR', _('Suriname')), 
    ('SJ', _('Svalbard and Jan Mayen')), 
    ('SZ', _('Swaziland')), 
    ('SE', _('Sweden')), 
    ('CH', _('Switzerland')), 
    ('SY', _('Syrian Arab Republic')), 
    ('TW', _('Taiwan, Province of China')), 
    ('TJ', _('Tajikistan')), 
    ('TZ', _('Tanzania, United Republic of')), 
    ('TH', _('Thailand')), 
    ('TL', _('Timor-Leste')), 
    ('TG', _('Togo')), 
    ('TK', _('Tokelau')), 
    ('TO', _('Tonga')), 
    ('TT', _('Trinidad and Tobago')), 
    ('TN', _('Tunisia')), 
    ('TR', _('Turkey')), 
    ('TM', _('Turkmenistan')), 
    ('TC', _('Turks and Caicos Islands')), 
    ('TV', _('Tuvalu')), 
    ('UG', _('Uganda')), 
    ('UA', _('Ukraine')), 
    ('AE', _('United Arab Emirates')), 
    ('GB', _('United Kingdom')),
    ('UM', _('United States Minor Outlying Islands')), 
    ('UY', _('Uruguay')), 
    ('UZ', _('Uzbekistan')), 
    ('VU', _('Vanuatu')), 
    ('VE', _('Venezuela')), 
    ('VN', _('Viet Nam')), 
    ('VG', _('Virgin Islands, British')), 
    ('VI', _('Virgin Islands, U.S.')), 
    ('WF', _('Wallis and Futuna')), 
    ('EH', _('Western Sahara')), 
    ('YE', _('Yemen')), 
    ('ZM', _('Zambia')), 
    ('ZW', _('Zimbabwe')), 
)

STATES = (
    ('FL', _('Florida')),
    ('AL', _('Alabama')),
    ('AK', _('Alaska')),
    ('AZ', _('Arizona')),
    ('AR', _('Arkansas')),
    ('CA', _('California')),
    ('CO', _('Colorado')),
    ('CT', _('Connecticut')),
    ('DE', _('Delaware')),
    ('DC', _('District of Columbia')),
    ('GA', pgettext_lazy('US state', 'Georgia')),
    ('HI', _('Hawaii')),
    ('ID', _('Idaho')),
    ('IL', _('Illinois')),
    ('IN', _('Indiana')),
    ('IA', _('Iowa')),
    ('KS', _('Kansas')),
    ('KY', _('Kentucky')),
    ('LA', _('Louisiana')),
    ('ME', _('Maine')),
    ('MD', _('Maryland')),
    ('MA', _('Massachusetts')),
    ('MI', _('Michigan')),
    ('MN', _('Minnesota')),
    ('MS', _('Mississippi')),
    ('MO', _('Missouri')),
    ('MT', _('Montana')),
    ('NE', _('Nebraska')),
    ('NV', _('Nevada')),
    ('NH', _('New Hampshire')),
    ('NJ', _('New Jersey')),
    ('NM', _('New Mexico')),
    ('NY', _('New York')),
    ('NC', _('North Carolina')),
    ('ND', _('North Dakota')),
    ('OH', _('Ohio')),
    ('OK', _('Oklahoma')),
    ('OR', _('Oregon')),
    ('PA', _('Pennsylvania')),
    ('RI', _('Rhode Island')),
    ('SC', _('South Carolina')),
    ('SD', _('South Dakota')),
    ('TN', _('Tennessee')),
    ('TX', _('Texas')),
    ('UT', _('Utah')),
    ('VT', _('Vermont')),
    ('VA', _('Virginia')),
    ('WA', _('Washington')),
    ('WV', _('West Virginia')),
    ('WI', _('Wisconsin')),
    ('WY', _('Wyoming')),
)



class AddressForm(forms.ModelForm):
    address_1 = forms.CharField(max_length=30, required = False)
    address_2 = forms.CharField(max_length=50, required = False)
    city = forms.CharField(max_length=60,required = False)
    state = forms.CharField(max_length=30,widget = forms.Select(choices=STATES), required = False)
    zip_code = forms.CharField(max_length=5, validators = [validate_zipcode],required = False)
    country = forms.CharField(max_length=50, widget = forms.Select(choices=COUNTRIES),required = False)

    class Meta:
        model = Address
        model.user = User
        fields = ['address_1','address_2','city','state','zip_code', 'country']
