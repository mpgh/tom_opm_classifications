from django.db import models
from tom_targets.models import Target

class TargetClassification(models.Model):
    '''
    Class representing a broker's classification of a target.

    :param target: The Target that this classification is assciated with.
    :type target: Target

    '''
    target = models.ForeignKey(Target, on_delete=models.CASCADE)
    source = models.TextField(blank=True, default='')
    level = models.TextField(blank=True, default='')
    classification = models.TextField(blank=True, default='')
    probability = models.FloatField(null=True, blank=True)
    mjd = models.FloatField(null=True, blank=True)

    def as_dict(self):
        return {
            'target': self.target,
            'broker': self.source,
            'level': self.level,
            'type': self.classification,
            'prob': self.probability,
            'mjd': self.mjd,
        }
        
    def __str__(self):
        s = f'{self.target}, {self.classification}, {self.probability}'
        return s