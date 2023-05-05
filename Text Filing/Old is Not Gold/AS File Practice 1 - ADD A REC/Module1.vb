Module Module1

    Sub Main()

        Dim rollNo As Integer
        Dim sName, sContact As String
        Dim sFee As Decimal
        Dim isFeePaid As Boolean

        Console.Write("Enter roll No. :")
        rollNo = Console.ReadLine

        Console.WriteLine("Enter Name :")
        sName = Console.ReadLine

        Console.Write("Enter contact :")
        sContact = Console.ReadLine

        Console.Write("Enter fee amount :")
        sFee = Console.ReadLine

        Console.Write("Is fee already paid? ")
        isFeePaid = Console.ReadLine

        FileOpen(1, "d:\filePractice\sRec.txt", OpenMode.Output)

        WriteLine(1, rollNo)
        WriteLine(1, sName)
        WriteLine(1, sContact)
        WriteLine(1, sFee)
        WriteLine(1, isFeePaid)


        FileClose(1)

        Console.ReadKey()

    End Sub

End Module
