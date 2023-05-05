Module Module1

    Sub Main()
        Dim GRNO As Integer
        Dim sName, sClass As String
        Dim sFee As Decimal
        Dim isFeePaid As Boolean
        Dim Address As String
        Dim Telephone As String

        GRNO = 0
        sName = ""
        sClass = ""
        sFee = 0
        isFeePaid = False
        Address = ""
        Telephone = ""

        FileOpen(1, "C:\filePractice\ABC.txt", OpenMode.Input)
        FileOpen(2, "C:\filePractice\ABC2.txt", OpenMode.Output)
        While Not EOF(1)
            GRNO = LineInput(1)
            Input(1, sName)
            Input(1, sClass)
            Input(1, sFee)
            Input(1, isFeePaid)

            Console.WriteLine("Enter GR No: " & GRNO)
            Console.WriteLine("Enter student name: " & sName)
            Console.WriteLine("Enter student class: " & sClass)
            Console.WriteLine("Enter fee amount: " & sFee)
            Console.WriteLine("Is fee paid? " & isFeePaid)

            Console.Write("Enter address: ") : Address = Console.ReadLine
            Console.Write("Enter telephone number: ") : Telephone = Console.ReadLine

            WriteLine(2, GRNO)
            WriteLine(2, sName)
            WriteLine(2, sClass)
            WriteLine(2, sFee)
            WriteLine(2, isFeePaid)
            WriteLine(2, Address)
            WriteLine(2, Telephone)
        End While
        FileClose(1)
        FileClose(2)
    End Sub

End Module
