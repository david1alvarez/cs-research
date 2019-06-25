using System;
using System.Collections.Generic;

namespace GradeBook
{
    class Program
    {
        static void Main(string[] args)
        {
            var book = new Book("David's Gradebook");
            book.AddGrade(90.1);
            book.AddGrade(89.1);
            book.AddGrade(77.5);
            var stats = book.GetStatistics();
            System.Console.WriteLine($"The lowest grade is {stats.Low}");
            System.Console.WriteLine($"The highest grade is {stats.High}");
            System.Console.WriteLine($"The average is {stats.Average:N1}");
            // book.grades.Add(101); --> illegale bacause grades is a private property of Book
            // in cmd, the command "dotnet run -- David" will pass in "David" into the Main() method
            // no arguments leads do an unhandled exception error due to attempting to access an 
            // index that does not exist (empty array)

            // var x = 34.1;
            // var y = 24.8;
            // var result = x + y;
            
            // declaring with an input in the array declaration limits the length to exactly that length
            // var numbers = new double[3] {12.7, 10.3, 6.11};
            // numbers[0] = 12.7;
            // numbers[1] = 10.3;
            // numbers[2] = 6.11;
        }
    }
}
