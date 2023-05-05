Module Module1
    Structure StuType
        <VBFixedString(15)> Dim Name As String
        <VBFixedString(3)> Dim SClass As String
        Dim age As Integer
        Dim SchFee As Decimal
        Dim hasFeePaid As Boolean
        Dim grade As Char
        Dim DOB As Date
    End Structure

    Sub Main()
        Dim choice As Integer
        Dim choP As Int16 = 0
        Dim thing As Boolean
        Dim recChoice As Integer

        choice = 0
        While choice <> 4
            Console.Clear()
            Console.WriteLine("Enter 1 to add record to the random file")
            Console.WriteLine("Enter 2 to read record from the random file")
            Console.WriteLine("Enter 3 to edit record of the random file")
            Console.WriteLine("Enter 4 to Exit")
            Console.Write("Your choice... ")
            choice = Console.ReadLine
            Select Case choice
                Case 1 : RecAdder()
                Case 2
                    Console.Write("Enter record number from the random file :")
                    recChoice = Console.ReadLine()
                    thing = RecSearcher(recChoice)
                    If Not thing Then
                        Console.WriteLine("Record not found")
                        Console.ReadKey()
                    End If
                Case 3
                    Console.Write("Enter record number from the random file :")
                    recChoice = Console.ReadLine()
                    thing = RecEditor(recChoice)
                    If Not thing Then
                        Console.WriteLine("Record not found")
                        Console.ReadKey()
                    End If
                Case 4
                Case Else
                    Console.WriteLine("Wrong choice made... Press any key to continue.")
                    Console.ReadKey()
            End Select
        End While
    End Sub

    Sub RecAdder()
        Dim S1 As StuType
        Console.Write("Enter student Name :")
        S1.Name = Console.ReadLine()
        Console.Write("Enter student Age :")
        S1.age = Console.ReadLine()
        Console.Write("Enter student class :")
        S1.SClass = Console.ReadLine()
        Console.Write("Enter student fee amount :")
        S1.SchFee = Console.ReadLine()
        Console.Write("Enter student has student paid fee :")
        S1.hasFeePaid = Console.ReadLine()
        Console.Write("Enter student grade :")
        S1.grade = Console.ReadLine()
        Console.Write("Enter student DOB :")
        S1.DOB = Console.ReadLine()
        Dim RecNum As Integer
        FileOpen(1, "d:\Zafar.rnd", OpenMode.Random, OpenAccess.ReadWrite, , Len(S1))
        RecNum = LOF(1) / Len(S1)
        RecNum = RecNum + 1
        FilePut(1, S1, RecNum)
        FileClose(1)
    End Sub

    Function RecSearcher(ByVal RN As Int16) As Boolean
        Dim S1 As StuType
        Dim RecNum As Integer
        FileOpen(1, "d:\Zafar.rnd", OpenMode.Random, OpenAccess.ReadWrite, , Len(S1))
        RecNum = LOF(1) / Len(S1)
        If RN > RecNum Then
            Return False
            Exit Function
        End If
        FileGet(1, S1, RN)
        FileClose(1)
        Console.WriteLine("Enter student Name :" & S1.Name)
        Console.WriteLine("Enter student Age :" & S1.age)
        Console.WriteLine("Enter student class :" & S1.SClass)
        Console.WriteLine("Enter student fee amount :" & S1.SchFee)
        Console.WriteLine("Enter student has student paid fee :" & S1.hasFeePaid)
        Console.WriteLine("Enter student grade :" & S1.grade)
        Console.WriteLine("Enter student DOB :" & S1.DOB)
        Console.ReadKey()
        Return True
    End Function

    Function RecEditor(ByVal RN As Int16) As Boolean
        Dim S1 As StuType

        Dim RecNum As Integer
        FileOpen(1, "d:\Zafar.rnd", OpenMode.Random, OpenAccess.ReadWrite, , Len(S1))

        RecNum = LOF(1) / Len(S1)
        If RN > RecNum Then
            Return False
            Exit Function
        End If

        FileGet(1, S1, RN)
        Console.WriteLine("Enter student Name :" & S1.Name)
        Console.WriteLine("Enter student Age :" & S1.age)
        Console.WriteLine("Enter student class :" & S1.SClass)
        Console.WriteLine("Enter student fee amount :" & S1.SchFee)
        Console.WriteLine("Enter student has student paid fee :" & S1.hasFeePaid)
        Console.WriteLine("Enter student grade :" & S1.grade)
        Console.WriteLine("Enter student DOB :" & S1.DOB)

        Dim x As Decimal
        Dim z As String

        Console.Write("Input student Name, enter to leave :")
        z = Console.ReadLine()
        If z <> "" Then S1.Name = z

        Console.Write("Input student Age, 0 to leave :")
        x = Console.ReadLine()
        If x <> 0 Then S1.age = x

        Console.Write("Input student class, enter to leave :")
        z = Console.ReadLine()
        If z <> "" Then S1.SClass = z

        Console.Write("Input student fee amount, enter 0 to leave :")
        x = Console.ReadLine()
        If x <> 0 Then S1.SchFee = x

        Console.Write("Input student has student paid fee, enter to leave :")
        z = Console.ReadLine()
        If z <> "" Then S1.hasFeePaid = z

        Console.Write("Input student grade, enter to leave :")
        z = Console.ReadLine()
        If z <> "" Then S1.grade = z

        Console.Write("Input student DOB, enter to leave :")
        z = Console.ReadLine()
        If z <> "" Then S1.DOB = z

        FilePut(1, S1, RN)
        FileClose(1)

        Return True
    End Function


End Module