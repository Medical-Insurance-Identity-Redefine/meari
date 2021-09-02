# MEARI

#여기에 우리 로고 이미지 넣어줘


```
🍎 2021 데이터청년캠퍼스 <빅리더 아카데미> 🍎

Big Leader Academy
- 2021. 06. 28 ~ 2021. 08. 30

AI를 활용한 비급여 진료비 자가점검 서비스😊
```


<br/>

## 목차

- [개발환경 및 사용한 라이브러리](#개발환경-및-사용한-라이브러리)

- [서비스 workflow](#서비스-workflow)

- [기능 개발여부/담당자](#기능-개발여부/담당자)

- [핵심기능 구현 방법](#핵심기능-구현-방법)

- [팀원 역할 및 소개](팀원-역할-및-소개)

- [새롭게 알게 된 것](#새롭게-알게-된-것)

### 개발환경 및 사용한 라이브러리

|                          라이브러리                          |               목적               |      |
| :----------------------------------------------------------: | :------------------------------: | ---- |
|       [RxSwift](https://github.com/ReactiveX/RxSwift)        |           비동기 처리            | SPM  |
|     [Kingfisher](https://github.com/onevcat/Kingfisher)      |           이미지 캐실            | SPM  |
|        [SnapKit](https://github.com/SnapKit/SnapKit)         |          오토 레이아웃           | SPM  |
|     [Alamofire](https://github.com/Alamofire/Alamofire)      |            서버 통신             | SPM  |
|           [Then](https://github.com/devxoul/Then)            | 컴포넌트 코드 작성의 용이를 위해 | SPM  |
|   [FSCalendar](https://github.com/WenchaoD/FSCalendar.git)   |           캘린더 사용            | SPM  |
| [SwiftKeychainWrapper](https://github.com/jrendel/SwiftKeychainWrapper) |          저장소 암호화           | SPM  |
| [YPImagePicker](https://github.com/Yummypets/YPImagePicker)  |           사진첩 사용            | SPM  |
| [RxKeyboard](https://github.com/RxSwiftCommunity/RxKeyboard) |         키보드 동적 사용         | SPM  |
| [Moya](https://github.com/Moya/Moya)                         |          서버 통신              | SPM  |
| [Lottie](https://github.com/airbnb/lottie-ios)               |          애니메이션 사용        | SPM  |
| [SegementSlide](https://github.com/Jiar/SegementSlide) | 탭바 사용 | CocoaPod |

<br>

### 서비스 workflow

#여기에 이미지 넣어줘



### 기능 개발여부/담당자

|    기술     |        기능        | 담당자 | 구현 여부 |
| :---------: | :---------------------: | :----: | :-------: |
|  데이터전처리   |        데이터정제         |  성현  |     ✅     |
|  OpenCV + OCR   |        서류읽어오기         |  주은  |     ✅     |
|   NLP    |         사전제작          |  기표  |     ✅     |
|  Machine Learning   |        예측모델제작        |  규영  |     ✅     |
|      어플제작       |        프로토타입         |  주은  |     ✅     |



### 파트별 중요 코드
1. 데이터전처리

   ~~~python
   // 캘린더 정보 저장을 위한 변수
   var calendarDictionary: [String : [FSCalendarModel]] = [:]
   
   guard let promise: [FSCalendarModel] = calendarDictionary[day] else { return UICollectionViewCell() }
   if promise[indexPath.row].isNotice == 0 {
     let cell: CalendarCollectionViewCell = collectionView.dequeueCell(forIndexPath: indexPath)
   	cell.calendar = promise[indexPath.row]
   	cell.fetchCalendar()
   	cell.fetchCategory()
   	cell.fetchTime()
   	return cell
   } else {
   	let cell: NoticeCollectionViewCell = collectionView.dequeueCell(forIndexPath: indexPath)
   	cell.calendar = promise[indexPath.row]
   	cell.fetchCalendar()
   	cell.fetchTime()
   	return cell
   }
   
   ~~~

2. OpenCV + OCR

   ```swift
   func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
   		let cell: MessageDetailTableViewCell = tableView.dequeueCell(forIndexPath: indexPath)
   		if self.userOrOwner == 0 {
   			if self.status[indexPath.row] == 0 {
   				cell.titleLabel.text = "문의사항이 등록되었어요!"
   				cell.contextLabel.attributedText = self.makeAttributed(
   					context: "아래의 버튼을 눌러\n약속시간을 정해보세요."
   				)
   				cell.transitionButton.addTarget(self,
   																				action: #selector(didTapConfirmButton(_:)),
   																				for: .touchUpInside
   				)
   				cell.transitionButton.setTitle("약속 확정하기", for: .normal)
   			}
   			else if self.status[indexPath.row] == 1 {
   				cell.titleLabel.text = "약속이 확정되었어요!"
   				var confirmedPromise = "\(self.confirmedPromiseOption)예정이에요\n 캘린더에서 일정을 확인해보세요."
   				cell.contextLabel.attributedText = self.makeAttributed(context: confirmedPromise)				
   				cell.transitionButton.addTarget(self,
   																				action: #selector(didTapCalendarButton(_:)),
   																				for: .touchUpInside)
   				cell.transitionButton.setTitle("캘린더 보기", for: .normal)
   			}
   			else if self.status[indexPath.row] == 2 {
   				cell.titleLabel.text = "약속 수정 요청을 보냈어요!"
   				cell.contextLabel.attributedText = self.makeAttributed(
   					context: "앞으로도 하우징과 함께\n자취생과 소통해보세요!"
   				)
   				cell.transitionButton.snp.makeConstraints {
   					$0.height.equalTo(0)
   				}
   			}
   			...
   ```

### 팀원 역할 및 소개

| <IMG src="https://https://github.com/yooseonghyeon.png?size=100" width="150"> | <IMG src="https://github.com/JubyKim.png?size=100" width="150"> | <IMG src="https://github.com/fluffyword.png?size=100" width="150">| <IMG src="https://https://github.com/Giggle1998.png?size=100" width="150"> |
| :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
|                            유성현                            |                            김주은                            |                            이규영                            |                            이기표                            |

