# How to Contribute to latrine

## Basics

1. Fork eputnam/latrine
1. Clone your fork
1. Create a new branch (`git checkout -b my_feature`)
1. Commit your changes (`git commit -m 'some changes'`)
1. Push to your fork
1. Open a pull request against eputnam/latrine:master

## Making a Pull Request

Pull requests are always weclome! To make the process easier on everyone, here are a few guidelines:

1. **Try to make keep commits small**
This helps everyone. It helps you divide up and organize your work and in the unfortunate event that your changes need to be reverted, it is helpful to have work divided into bite-size chunks so that only the parts that need to be reverted get reverted.
1. **Commit messages are important**
A good commit message is like...a good commit message! Easy to read and concise yet informative. If you're looking for guidelines, [this page](https://chris.beams.io/posts/git-commit/) has some pretty good ones. If you don't feel like reading that, here are a few questions to get you started.

* What is the current behavior?
* Why does it need to be changed?
* How did you change it?

In your message, please include a short, descriptive title and include answers to the above questions in the body.

## Reviewing/Merging a Pull Request
This section is for those who have push access to the repository.

* Is this a new feature? A bugfix? Is it a backwards incompatible?
* Does this change need tests? Does the PR include tests?
* Should the documentation be updated for this change?
* _Do Not Merge Your Own Pull Request_
It's common and good practice to have someone else hit that big green button. Why bother with a pull request if not to have someone else review and merge your work? This is a group/community project so not only is it important to have someone else do a sanity check on your work, but others should have a chance to weigh in on your code if they want to.

## Documentation

If you are adding a new feature or changing the way latrine works, it may be necessary to document it in the README or elsewhere. Please be sure that you do so along with your changes.
