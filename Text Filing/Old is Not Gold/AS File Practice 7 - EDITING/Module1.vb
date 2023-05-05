Module Module1

    Sub Main()
        'File Record Deletion
        Dim rollNo, searchRollNo As Integer
        Dim sName, sContact As String
        Dim sFee As Decimal
        Dim isFeePaid, isFound As Boolean
        isFound = False

        Console.Write("Enter roll# to edit:")
        searchRollNo = Console.ReadLine
        FileOpen(1, "c:\filePractice\sRec.txt", OpenMode.Input)
        FileOpen(2, "c:\filePractice\temp.txt", OpenMode.Output)

        While Not EOF(1)
            Input(1, rollNo)
            Input(1, sName)
            Input(1, sContact)
            Input(1, sFee)
            Input(1, isFeePaid)
            If rollNo <> searchRollNo Then
                WriteLine(2, rollNo)
                WriteLine(2, sName)
                WriteLine(2, sContact)
                WriteLine(2, sFee)
                WriteLine(2, isFeePaid)
            ElseIf rollNo = searchRollNo Then
                isFound = True

                Console.WriteLine("Enter student name: ")
                sName = Console.ReadLine

                Console.Write("Enter student contact: ")
                sContact = Console.ReadLine

                Console.Write("Enter fee amount: ")
                sFee = Console.ReadLine

                Console.Write("Is fee paid? ")
                isFeePaid = Console.ReadLine

                WriteLine(2, searchRollNo)
                WriteLine(2, sName)
                WriteLine(2, sContact)
                WriteLine(2, sFee)
                WriteLine(2, isFeePaid)
            End If
        End While
        FileClose(1)
        FileClose(2)
        My.Computer.FileSystem.DeleteFile("c:\filePractice\sRec.txt")
        My.Computer.FileSystem.RenameFile("c:\filePractice\temp.txt", _
                                          "sRec.txt")
        If isFound = False Then Console.WriteLine("Record not found...")


        Console.ReadKey()

    End Sub

End Module
