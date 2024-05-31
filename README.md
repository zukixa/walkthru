# walkthru

Welcome to the **walkthru!** This repository serves as a practical walkthrough of implementing software using the Test-Driven Development (TDD) approach, specifically demonstrating the red-green-refactor cycle & equivalence partioning. As you navigate through the commit history of this repository, you will see my thought processes and developmental iterations captured step-by-step, offering insights into each stage of the code development.

## Overview

The **walkthru** repository is a part of the broader [home-of-tdd](https://github.com/zukixa/home-of-tdd) GitHub repostiroy project where you can find more educational content on TDD and related software development methodologies.
Each commit in this repository is thoughtfully commented to reflect on the changes made and the reasoning behind each decision. This ensures that observers can follow along with the development process as if they were part of the coding journey themselves.

### Educational Objective

This repository aims to provide real-world insights into how TDD is implemented and how it can lead to more robust, bug-free code. By following the red-green-refactor pattern, I demonstrate how to:
- Initiate a test (Red: write a failing test, which covers a partition determined by equivalence partitioning)
- Make the test pass (Green: write just enough code to make the test pass)
- Refactor the code (Refactor: clean up the code while keeping the tests passing)

## Utilized Resources

Throughout the development process, I utilized the following Code Review Checklist to ensure quality and adherence to best practices: [Code Review Checklist](https://docs.google.com/document/d/19nxIcbU1EAnlspBsbi1MKjjdgyByauv-r7fc6WrZXMw/edit)
This checklist was instrumental in guiding the refactor phases and ensuring that each step met high standards.

## How to Use This Repository

- **Review the Commit History**: Navigate through the commit history to understand the incremental development and TDD steps implemented. Each commit message and description detail the purpose and context of the changes.
- **Explore Each Branch**: The branches represent different features or components developed through TDD practices.
- **Read the Comments**: Each commit includes detailed comments discussing the changes, why they were made, and occasionally what could be improved or considered in future iterations.
- **Follow the Checklist:** If you ever are struggling with the process, refer to the checklist below for guidance!
----
### walkthru-checklist:

#### **Red Phase**
- Group your test cases into partitions that should behave the same way.
- Pick a test case from a group.
- Write that test for what you want to add or fix.
- Check that the test does not pass yet.

#### **Green Phase**
- Write the simplest code that makes the test pass.

#### **Refactor Phase**
- Look at your new code and clean it up without changing how it works.
- Make sure your test still passes after cleaning up the code.

#### **Overall:**
  - Always run your tests to check everything still works.
  - Save your changes often with notes on what you did.
  - Do this for every new thing you want to add or fix.

-----
Enjoy exploring TDD with **walkthru**!
