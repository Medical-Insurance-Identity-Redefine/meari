//
//  ExtensionVC.swift
//  uploadImage
//
//  Created by JUEUN KIM on 2021/08/22.
//

import UIKit



class ExtensionVC: UIViewController {

    override func viewDidLoad() {

        super.viewDidLoad()

    }

}



extension UIViewController {

    class func displaySpinner(onView: UIView) -> UIView {

        let spinnerView = UIView.init(frame: onView.bounds)
        let loadingLabel = UILabel()
        
        loadingLabel.text = "환불가능성을 계산중입니다."
        spinnerView.backgroundColor = UIColor.init(red: 0.5, green: 0.5, blue: 0.5, alpha: 1.0)

        let ai = UIActivityIndicatorView.init(style: .whiteLarge)

        ai.startAnimating()

        ai.center = spinnerView.center

        DispatchQueue.main.async {
            
            spinnerView.addSubview(ai)
            onView.addSubview(spinnerView)
        }

        return spinnerView
    }

    

    class func removeSpinner(spinner : UIView) {
        DispatchQueue.main.async {
            spinner.removeFromSuperview()
        }
    }

}
