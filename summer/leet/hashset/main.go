package main

import "fmt"

type MyHashSet struct {
    hashmap map[int]bool
}


func Constructor() MyHashSet {
	m := MyHashSet{
		hashmap: make(map[int]bool),
	}
    return m
}


func (this *MyHashSet) Add(key int)  {
    if !this.Contains(key){
		this.hashmap[key]=true
	}
}


func (this *MyHashSet) Remove(key int)  {
    if this.Contains(key){
		delete(this.hashmap, key)
	}
	
}


func (this *MyHashSet) Contains(key int) bool {
	_ , ok := this.hashmap[key]
	return ok
}


/**
 * Your MyHashSet object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Add(key);
 * obj.Remove(key);
 * param_3 := obj.Contains(key);
 */

func main() {
	fmt.Println("Hello")
	obj := Constructor();
	obj.Add(1);
	obj.Remove(2);
	param_3 := obj.Contains(1);
	fmt.Println(param_3)
}