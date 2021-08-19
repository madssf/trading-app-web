from apps.currencies.models import TagGroup, Tag, CurrencyTag

def is_stablecoin(currency_obj):
  try:
    stablecoin_tags = Tag.objects.filter(tag_group=TagGroup.objects.get(name="Stablecoin"))
    if len(stablecoin_tags) < 1:
      return False
    for tag in stablecoin_tags:
      try:
        return len(CurrencyTag.objects.get(currency=currency_obj, tag=Tag.objects.get(name=tag.name))) > 0
      except (CurrencyTag.DoesNotExist, Tag.DoesNotExist):
        return False
  except Tag.DoesNotExist:
    return False