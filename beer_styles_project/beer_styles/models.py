from django.db import models
from decimal import Decimal, ROUND_HALF_UP

class BeerStyle(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=10)
    category = models.CharField(max_length=100)
    categorynumber = models.CharField(max_length=10)
    overallimpression = models.TextField(null=True, blank=True)
    aroma = models.TextField(null=True, blank=True)
    appearance = models.TextField(null=True, blank=True)
    flavor = models.TextField(null=True, blank=True)
    mouthfeel = models.TextField(null=True, blank=True)
    comments = models.TextField(null=True, blank=True)
    history = models.TextField(null=True, blank=True)
    characteristicingredients = models.TextField(null=True, blank=True)
    stylecomparison = models.TextField(null=True, blank=True)
    ibumin = models.DecimalField(max_digits=8, decimal_places=2,null=True, blank=True)
    ibumax = models.DecimalField(max_digits=8, decimal_places=2,null=True, blank=True)
    ogmin = models.DecimalField(max_digits=8, decimal_places=4,null=True, blank=True)
    ogmax = models.DecimalField(max_digits=8, decimal_places=4,null=True, blank=True)
    fgmin = models.DecimalField(max_digits=8, decimal_places=4,null=True, blank=True)
    fgmax = models.DecimalField(max_digits=8, decimal_places=4,null=True, blank=True)
    abvmin = models.DecimalField(max_digits=8, decimal_places=2,null=True, blank=True)
    abvmax = models.DecimalField(max_digits=8, decimal_places=2,null=True, blank=True)
    srmmin = models.DecimalField(max_digits=8, decimal_places=2,null=True, blank=True)
    srmmax = models.DecimalField(max_digits=8, decimal_places=2,null=True, blank=True)
    commercialexamples = models.TextField(null=True, blank=True)
    tags = models.TextField(null=True, blank=True)
    entryinstructions = models.TextField(null=True, blank=True)
    currentlydefinedtypes = models.TextField(null=True, blank=True)
    strengthclassifications = models.TextField(null=True, blank=True)
    overallimpression_cz = models.TextField(null=True, blank=True)
    aroma_cz = models.TextField(null=True, blank=True)
    appearance_cz = models.TextField(null=True, blank=True)
    flavor_cz = models.TextField(null=True, blank=True)
    mouthfeel_cz = models.TextField(null=True, blank=True)
    comments_cz = models.TextField(null=True, blank=True)
    history_cz = models.TextField(null=True, blank=True)
    characteristicingredients_cz = models.TextField(null=True, blank=True)
    stylecomparison_cz = models.TextField(null=True, blank=True)
    commercialexamples_cz = models.TextField(null=True, blank=True)
    tags_cz = models.TextField(null=True, blank=True)
    entryinstructions_cz = models.TextField(null=True, blank=True)
    currentlydefinedtypes_cz = models.TextField(null=True, blank=True)
    strengthclassifications_cz = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    # Vypočítané hodnoty
    @property
    def ebcmin(self):
        if self.srmmin is not None:
            try:
                ebc_value = self.srmmin * Decimal('1.97')
                return ebc_value.quantize(Decimal('1'), rounding=ROUND_HALF_UP)
            except:
                return None
        else:
            return None

    @property
    def ebcmax(self):
        if self.srmmax is not None:
            try:
                ebc_value = self.srmmax * Decimal('1.97')
                return ebc_value.quantize(Decimal('1'), rounding=ROUND_HALF_UP)
            except:
                return None
        else:
            return None

    @property
    def brixmin(self):
        if self.ogmin is not None:
            try:
                brix_value = Decimal(261.3) * (1 - 1 / self.ogmin)
                return brix_value.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
            except:
                return None
        else:
            return None

    @property
    def brixmax(self):
        if self.ogmax is not None:
            try:
                brix_value = Decimal(261.3) * (1 - 1 / self.ogmax)
                return brix_value.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
            except:
                return None
        else:
            return None
