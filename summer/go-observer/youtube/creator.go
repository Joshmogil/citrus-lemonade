package youtube

import (
	"observer/pubsub"
)

type Creator struct {
	Name string
	Subscribers []pubsub.Subscriber
}

//for each subsriber in c.Subscribers, call that subscriber's NotificationAction
func (c *Creator) Publish() {
	for _, sub := range c.Subscribers {
		message := "New video from " + c.Name
		sub.NotificationAction(message)
	}
}

func (c *Creator) AddSubscriber(sub pubsub.Subscriber) bool {
	c.Subscribers = append(c.Subscribers,sub)
	return true
}

func (c *Creator) ListSubscribers() []pubsub.Subscriber {
	return c.Subscribers
}