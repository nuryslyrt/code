class LogicGate:
    def __init__(self,n):
        self.label = n
        self.output = None
    def getLabel(self):
        return self.label
    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output
    class BinaryGate(LogicGate):
        def __init__(self,n):
            LogicGate.__init__(self,n)
            self.pinA = None
            self.pinB = None
        def getPinA(self):
            return input("Enter Pin A input for gate "+ \
            self.getLabel()+"-->")
        def getPinB(self):
            return input("Enter Pin B input for gate "+ \
            self.getLabel()+"-->")
        class UnaryGate(LogicGate):
            def __init__(self,n):
                LogicGate.__init__(self,n)
                self.pin = None
            def getPin(self):
                return input("Enter Pin input for gate "+ \
                self.getLabel()+"-->")
            
        class AndGate(BinaryGate):
            def __init__(self,n):
                BinaryGate.__init__(self,n)
            def performGateLogic(self):
                a = self.getPinA()
                b = self.getPinB()
                if a==1 and b==1:
                    return 1
                else:
                    return 0
        class Connector:
            def __init__(self, fgate, tgate):
                self.fromgate = fgate
                self.togate = tgate
                tgate.setNextPin(self)
            def getFrom(self):
                return self.fromgate
            def getTo(self):
                return self.togate
            def setNextPin(self,source):
                if self.pinA == None:
                    self.pinA = source
                else:
                    if self.pinB == None:
                        self.pinB = source
                    else:
                        print "Cannot Connect: NO EMPTY PINS"

            

