from rich.progress import track

def progress(iterable, description: str):
  return track(iterable, description=description)