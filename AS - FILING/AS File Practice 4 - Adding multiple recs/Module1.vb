Module Module1

    Sub Main()
        Dim rollNo As Integer
        Dim sName, sContact As String
        Dim sFee As Decimal
        Dim isFeePaid, moreRecs As Boolean

        FileOpen(1, "c:\filePractice\sRec.txt", OpenMode.Append)

        Do
            Console.Write("Enter roll number: ")
            rollNo = Console.ReadLine

            Console.WriteLine("Enter student name: ")
            sName = Console.ReadLine

            Console.Write("Enter student contact: ")
            sContact = Console.ReadLine

            Console.Write("Enter fee amount: ")
            sFee = Console.ReadLine

            Console.Write("Is fee paid? ")
            isFeePaid = Console.ReadLine

            WriteLine(1, rollNo)
            WriteLine(1, sName)
            WriteLine(1, sContact)
            WriteLine(1, sFee)
            WriteLine(1, isFeePaid)

            Console.Write("Want to ad next record? True/false: ")
            moreRecs = Console.ReadLine
        Loop Until moreRecs = False

        FileClose(1)
    End Sub

End Module
