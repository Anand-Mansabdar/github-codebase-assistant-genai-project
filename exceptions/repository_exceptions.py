class RepositoryError(Exception):
  """Base exception for all repository related errors."""
  

class InvalidRepositoryURLError(RepositoryError):
  pass

class RepositoryCloneError(RepositoryError):
  pass

class RepositoryAlreadyExistsError(RepositoryError):
  pass