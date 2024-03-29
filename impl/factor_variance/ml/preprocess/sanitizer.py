from ml.constant import exclude_domains

class Sanitizer:
  _EXCLUDE_DOMAINS = [
    '@example.com',
    '@g.example.com'
  ]

  @classmethod
  def sanitize(cls, data):
    d = cls._exclude_by_email_domain(data)
    # add another sanitizing if you need
    return d

  """
    exclude email, domain included _EXCLUDE_DOMAINS
  """
  @classmethod
  def _exclude_by_email_domain(cls, data):
    return data[~data['email'].str.contains('|'.join(cls._EXCLUDE_DOMAINS))]

