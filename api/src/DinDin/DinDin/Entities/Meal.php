<?php
namespace DinDin\DinDin\Entities;
/**
 * @Entity @Table(name="meals")
 **/
class Meal implements \JsonSerializable
{
    /** @Id @Column(type="integer") @GeneratedValue **/
    protected $id;

    /** @Column(type="string") **/
    protected $name;

    /** @Column(type="text") **/
    protected $description;

    /** @Column(type="string") **/
    protected $image;

    /** @Column(type="decimal") **/
    protected $price;

    public function getId()
    {
        return $this->id;
    }

    public function getName()
    {
        return $this->name;
    }

    public function setName($name)
    {
        $this->name = $name;
    }

    public function getImage()
    {
        return $this->image;
    }

    public function setImage($image)
    {
        $this->image = $image;
    }

    public function getDescription()
    {
        return $this->description;
    }

    public function setDescription($description)
    {
        $this->description = $description;
    }

    public function setStatus($status)
    {
        $this->status = $status;
    }

    public function getStatus()
    {
        return $this->status;
    }

    public function setPrice($price)
    {
        $this->price = $price;
    }

    public function getPrice()
    {
        return $this->price;
    }

    public function jsonSerialize() {
        $info = array();

        $info['id']          = $this->getId();
        $info['name']        = $this->getName();
        $info['description'] = $this->getDescription();
        $info['image']       = $this->getImage();
        $info['price']       = $this->getPrice();

        return $info;
    }
}