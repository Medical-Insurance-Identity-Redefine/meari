//
//  FirstViewController.swift
//  uploadImage
//
//  Created by JUEUN KIM on 2021/08/22.
//

import UIKit

class FirstViewController: UIViewController {
    @IBOutlet var bigView: UIView!
    @IBOutlet var applicantView: UIView!
    @IBOutlet var moneyView: UIView!
    @IBOutlet var processView: UIView!

    @IBOutlet var homePageButton: UIButton!
    @IBOutlet var noRefundButton: UIButton!
    @IBOutlet var callButton: UIButton!
    
    @IBAction func noRefundTapped(_ sender: Any) {
        guard let appleUrl = URL(string: "https://www.hira.or.kr/dummy.do?pgmid=HIRAA010002090100&cmsurl=/cms/medi_exp/01/1352739_26954.html")   else { return }
        guard UIApplication.shared.canOpenURL(appleUrl)             else { return }

        UIApplication.shared.open(appleUrl, options: [:], completionHandler: nil)
    }
    @IBAction func homePageTapped(_ sender: Any) {
        guard let appleUrl = URL(string: "https://www.hira.or.kr/re/diag/hospitalTeme.do?pgmid=HIRAA030009040000")   else { return }
        guard UIApplication.shared.canOpenURL(appleUrl)             else { return }

        UIApplication.shared.open(appleUrl, options: [:], completionHandler: nil)
    }
    
    
    
    @IBAction func callTapped(_ sender: Any) {
        let number:Int = 337391433 //심평원 진료비확인부 번호
                
                // URLScheme 문자열을 통해 URL 인스턴스를 만들어 줍니다.
                if let url = NSURL(string: "tel://0" + "\(number)"),
                
                   //canOpenURL(_:) 메소드를 통해서 URL 체계를 처리하는 데 앱을 사용할 수 있는지 여부를 확인
                   UIApplication.shared.canOpenURL(url as URL) {
                   
                   //사용가능한 URLScheme이라면 open(_:options:completionHandler:) 메소드를 호출해서
                   //만들어둔 URL 인스턴스를 열어줍니다.
                    UIApplication.shared.open(url as URL, options: [:], completionHandler: nil)
                }
    }
    func makeShadow(yourView: UIView){
        yourView.layer.shadowColor = UIColor.black.cgColor
        yourView.layer.shadowOpacity = 1
        yourView.layer.shadowOffset = .zero
        yourView.layer.shadowRadius = 10
    }
    override func viewDidLoad() {
        super.viewDidLoad()
        
        self.bigView.layer.cornerRadius = 15
        self.bigView.clipsToBounds = true
        self.applicantView.layer.cornerRadius = 15
        self.applicantView.clipsToBounds = true
        self.moneyView.layer.cornerRadius = 15
        self.moneyView.clipsToBounds = true
        self.processView.layer.cornerRadius = 15
        self.processView.clipsToBounds = true
        
        self.homePageButton.layer.cornerRadius = 15
        self.homePageButton.clipsToBounds = true
        
        self.noRefundButton.layer.cornerRadius = 15
        self.noRefundButton.clipsToBounds = true
        
        self.callButton.layer.cornerRadius = 15
        self.callButton.clipsToBounds = true
        
        
        makeShadow(yourView: self.bigView)
        makeShadow(yourView: self.applicantView)
        makeShadow(yourView: self.moneyView)
        makeShadow(yourView: self.processView)

    }

}
