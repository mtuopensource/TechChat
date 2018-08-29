# Android Testing *( What are they, and how to run them)*


## Overview on testing setup

Currently all testing for the android client code is split into two categories:

  1. Unit Test
  2. Instrumentation Test

Unit test test a single unit of code. Ie a class, or method. They should simple to make and simple to edit. They can be found in test directory in the client src.


Unit test should  stress any input a class or method may encounter. When a bug is found, a unit should be created to stress the bug behaviour. This will help the prevent regression of bugs


Instrumentation tests ,on the other hand, test multiple unit working together. This will manifest into automated ui test. While the ui test look fancy, they test code that cannot be tested by unit test as they rely on a running application environment.

Just like unit test, instrumentation test should be simple to edit and read. Android expresso test library is confusing to learn and read, so make sure you have comments that go through each step in the test. (This may help you see bug or flaws in your test).



## How to run the tests

1. Unit Test

Running the unit test is fairly simple. If you are familiar with any junit test suite, then you will be right at home. In Android Studio its as simple as clicking the green arrow on a unit test class.

If you want to run all of the unit test in the suite, run the "test" gradle task. This can be done in android studio by opening the gradle tab and double clicking the test task. If will only tell you if test fail, otherwise the task will complete

2. Instrumentation Test

**To run these test you will need either an android phone, and a way to hook it up to your computer, or a running emulator.**

Similarly to the unit test, you can run single test by clicking the green arrow from the instrumentation test class. To run all the instrumentation task, use the "connectedAndroidTest" gradle task. 

 * Note: For these test to run properly, make sure you have all animation on your phone disabled. Some test may fail because of the animations. The error message should tell you if that is the case

