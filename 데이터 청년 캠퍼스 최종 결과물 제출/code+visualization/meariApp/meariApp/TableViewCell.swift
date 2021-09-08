//
//  TableViewCell.swift
//  meariApp
//
//  Created by JUEUN KIM on 2021/08/27.
//

import UIKit

class TableViewCell: UITableViewCell {
    let identifier = "TableViewCell"
    @IBOutlet var codeView: UIView!
    @IBOutlet var label: UILabel!
    
    override func awakeFromNib() {
        super.awakeFromNib()
        // Initialization code
    }

    override func setSelected(_ selected: Bool, animated: Bool) {
        super.setSelected(selected, animated: animated)

        // Configure the view for the selected state
    }
    

}
