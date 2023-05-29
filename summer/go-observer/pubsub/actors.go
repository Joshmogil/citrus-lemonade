package pubsub

type Subscriber interface {
	Subscribe(Publisher) bool
	GetSubscriptions() []Publisher
	NotificationAction(message string) 
}

type Publisher interface {
	Publish()
	AddSubscriber(Subscriber) bool
	ListSubscribers() []Subscriber
}

