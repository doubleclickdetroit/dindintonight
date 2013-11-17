<?php
/**
 * @Entity @Table(name="meals")
 **/
class Meal
{
    /** @Id @Column(type="integer") @GeneratedValue **/
    protected $id;

    /** @Column(type="string") **/
    protected $name;

    /** @Column(type="string") **/
    protected $status;

    /** @Column(type="string") **/
    protected $description;

    /** @Column(type="boolean") **/
    protected $vegetarian;

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

    public function setVegetarian($vegetarian)
    {
        $this->vegetarian = $vegetarian;
    }

    public function getVegetarian()
    {
        return $this->vegetarian;
    }
}
