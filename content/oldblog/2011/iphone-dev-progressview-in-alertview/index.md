---
title: iOS 在 UIAlertView 中显示进度条
slug: iphone-dev-progressview-in-alertview
date: '2011-12-09T18:27:00+08:00'
lastmod: '2011-12-21T10:31:00+08:00'
tags:
- iOS Develop
categories:
- 程序开发
summary: 今天这个问题是，在一个 iPhone 程序中，我要在后台做大量的数据处理，希望在界面上显示一个进度条（Progress Bar）使得用户了解处理进度。这个进度条应该是在一个模态的窗口中，使界面上其他控件无法被操作。怎么用最简单的方法来实现这个功能？UIAlertView
  是一个现成的模态窗口，如果能把进度条嵌入到它里面就好了。
keywords:
- iPhone 开发
- ObjC
- progress bar
- UIAlertView
- UIProgressView
- 进度条
---

今天这个问题是，在一个 iPhone 程序中，我要在后台做大量的数据处理，希望在界面上显示一个进度条（Progress
Bar）使得用户了解处理进度。这个进度条应该是在一个模态的窗口中，使界面上其他控件无法被操作。怎么用最简单的方法来实现这个功能？[UIAlertView](http://developer.apple.com/library/ios/#documentation/UIKit/Reference/UIAlertView_Class/UIAlertView/UIAlertView.html) 是一个现成的模态窗口，如果能把进度条嵌入到它里面就好了。

以下内容适用于 iOS 2\.0\+。

我们知道，如果要显示一个 alert 窗口（比如用来显示错误或警告信息、询问用户是否确认某操作等等），只要简单地创建一个 UIAlertView 对象，再调用其 show 方法即可。示意代码如下：

```objc {linenos=table}
UIAlertView* alertView = [[[UIAlertView alloc] initWithTitle:@"Title"
                                                     message:@"Message"
                                                    delegate:nil
                                           cancelButtonTitle:@"OK"
                                           otherButtonTitles:nil]
                          autorelease];
[alertView show];
```

如果要添加一个进度条，只要先创建并设置好一个 [UIProgressView](http://developer.apple.com/library/ios/#documentation/UIKit/Reference/UIProgressView_Class/Reference/Reference.html) 的实例，再利用 addSubbiew 方法添加到 alertView 中即可。

在实际应用中，我可能需要在类中保存进度条的对象实例，以便更新其状态，因此先在自己的 ViewController 类中添加成员变量：

```objc {linenos=table}
//  MySampleViewController.h
#import <UIKit/UIKit.h>

@interface MySampleViewController : UIViewController {
@private
    UIProgressView* progressView_;
}

@end
```

接下来写一个叫做 showProgressAlert 的方法来创建并显示带有进度条的 alert 窗口，其中高亮的部分就是把进度条添加到 alertView 中：

```objc {linenos=table hl_lines="9 10 11"}
- (void)showProgressAlert:(NSString*)title withMessage:(NSString*)message {
    UIAlertView* alertView = [[[UIAlertView alloc] initWithTitle:title
                                                         message:message
                                                        delegate:nil
                                               cancelButtonTitle:nil
                                               otherButtonTitles:nil]
                              autorelease];

    progressView_ = [[UIProgressView alloc] initWithProgressViewStyle:UIProgressViewStyleBar];
    progressView_.frame = CGRectMake(30, 80, 225, 30);
    [alertView addSubview:progressView_];

    [alertView show];
}
```

为了让数据处理的子进程能够方便地修改进度条的值，再添加一个简单的方法：

```objc {linenos=table}
- (void)updateProgress:(NSNumber*)progress {
    progressView_.progress = [progress floatValue];
}
```

另外，数据处理完毕后，我们还需要让进度条以及 alertView 消失，由于之前并没有保存 alertView 的实例，可以通过进度条的 superview 访问之：

```objc {linenos=table}
- (void)dismissProgressAlert {
    if (progressView_ == nil) {
        return;
    }

    if ([progressView_.superview isKindOfClass:[UIAlertView class]]) {
        UIAlertView* alertView = (UIAlertView*)progressView_.superview;
        [alertView dismissWithClickedButtonIndex:0 animated:NO];
    }

    [progressView_ release];
    progressView_ = nil;
}
```

假设处理数据的方法叫 processData，当然它会在一个单独的线程中运行，下面的片段示意了如何更新进度条状态，以及最后如何让它消失。

```objc {linenos=table}
- (void)processData:(int)total {
    for (int i = 0; i < total; ++i) {
        // Update UI to show progess.
        float progress = (float)i / total;
        NSNumber* progressNumber = [NSNumber numberWithFloat:progress];
        [self performSelectorOnMainThread:@selector(updateProgress:)
                               withObject:progressNumber
                            waitUntilDone:NO];

        // Process.
        // do it.
    }

    // Finished.
    [self performSelectorOnMainThread:@selector(dismissProgressAlert)
                           withObject:nil
                        waitUntilDone:YES];
    // Other finalizations.
}
```

在实际使用中，带进度条的 alert view 大概长得是这样的：

{{< image src="progress_alert.png" alt="progress_alert" caption="带进度条的 alert 窗口" >}}

---

参考：

- [UIProgressView in UIAlertView?](https://discussions.apple.com/thread/1737797)
