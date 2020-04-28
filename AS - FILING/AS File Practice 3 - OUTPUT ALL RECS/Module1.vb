Module Module1

    Sub Main()

        Dim rollNo As Integer
        Dim sName, sContact As String
        Dim sFee As Decimal
        Dim isFeePaid As Boolean

        FileOpen(1, "c:\filePractice\sRec.txt", OpenMode.Input)

        While Not EOF(1)

            Input(1, rollNo)
            Input(1, sName)
            Input(1, sContact)
            Input(1, sFee)
            Input(1, isFeePaid)

            Console.WriteLine("Student roll no. :" & rollNo)
            Console.WriteLine("Student name :" & sName)
            Console.WriteLine("Student contact :" & sContact)
            Console.WriteLine("Student fee amount Rs." & sFee)
            Console.WriteLine("Is Fee Paid? " & isFeePaid)

        End While

        FileClose(1)








        Console.ReadKey()

    End Sub

End Module
