from pathlib import Path
from dataclasses import dataclass, field

@dataclass
class FunctionInfo:
  name: str
  start_line: int
  end_line: int
  
@dataclass
class ClassInfo:
  name: str
  start_line: int
  end_line: int
  methods: list[FunctionInfo] = field(default_factory=list)
  
@dataclass
class CodeStructure:
  file_path: Path
  language: str
  imports: list[str] = field(default_factory=list)
  functions: list[FunctionInfo] = field(default_factory=list)
  classes: list[ClassInfo] = field(default_factory=list)