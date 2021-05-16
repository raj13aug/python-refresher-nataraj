class Device:
  def __init__(self, name, connected_by):
    self.name = name
    self.connected_by = connected_by
    self.connected = True
	   
  def __str__(self):
    return f"Device {self.name!r} ({self.connected_by})"
	  
  def disconnect(self):
	   self.connected = False
	   print("Disconnected")
	   
	   
class Printer(Device):
  def __init__(self, name, connected_by, capacity):
    super().__init__(name, connected_by)
    self.capacity = capacity
    self.remaining_pages = capacity
	
  def __str(self):
    return f"{super.__init__()}({self.remaining_pages} page remaining)"
	   
  def print(self, pages):
    if not self.connected:
      print("your printer is not connected!")
      return
    print(f"Printing {pages} pages")
    self.remaining_pages -= pages
		
printer = Printer("Printer", "usb", 500)
printer.print(20)

print(printer)
