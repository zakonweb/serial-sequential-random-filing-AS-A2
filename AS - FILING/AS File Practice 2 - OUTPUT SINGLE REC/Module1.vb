Module Module1

    Sub Main()

        Dim rollNo As Integer
        Dim sName, sContact As String
        Dim sFee As Decimal
        Dim isFeePaid As Boolean


        FileOpen(1, "c:\filePractice\sRec.txt", OpenMode.Input)


        Input(1, rollNo)
        Input(1, sName)
        Input(1, sContact)
        Input(1, sFee)
        Input(1, isFeePaid)

        Console.WriteLine("Roll Number: " & rollNo)
        Console.WriteLine("Name: " & sName)
        Console.WriteLine("Contact: " & sContact)
        Console.WriteLine("Fee Amount: " & sFee)
        Console.WriteLine("Fee Paid? " & isFeePaid)
        FileClose(1)

        Console.ReadKey()






    End Sub

End Module
