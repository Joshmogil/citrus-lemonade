package youtube

import (
	"fmt"
	"observer/pubsub"
)

type Viewer struct {
	Name string
	Subscriptions []pubsub.Publisher
}

func (v *Viewer) Subscribe(p pubsub.Publisher) bool {
	p.AddSubscriber(v)
	return true
}

func (v *Viewer) GetSubscriptions() []pubsub.Publisher {
	return v.Subscriptions
}


func (v *Viewer) NotificationAction(msg string) {
	fmt.Printf("My name is %s, and I recieved the following notification: %s\n", v.Name, msg)
}