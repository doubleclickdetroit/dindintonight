<?php
namespace DinDin\DinDin\Entities;
/**
 * @Entity @Table(name="locations")
 *
 */
class Location implements \JsonSerializable
{
    /**
     * @Id
     * @Column(type="integer")
     * @GeneratedValue
     *
     * @var int
     */
    protected $id;

    /**
     * @Column(type="string")
     *
     * @var string
     */
    protected $name;

    /**
     * @Column(type="string")
     *
     * @var string
     */
    protected $address;

    /**
     * @Column(type="string")
     *
     * @var string
     */
    protected $city;

    /**
     * @Column(type="string")
     *
     * @var string
     */
    protected $state;

    /**
     * @Column(type="string")
     *
     * @var string
     */
    protected $zip;

    /**
     * @ManyToMany(targetEntity="Meal")
     * @JoinTable(name="locations_meals",
     *      joinColumns={@JoinColumn(name="location_id", referencedColumnName="id")},
     *      inverseJoinColumns={@JoinColumn(name="meal_id", referencedColumnName="id")}
     * )
     */
    protected $meals;

    public function __construct()
    {
        $this->meals = new \Doctrine\Common\Collections\ArrayCollection();
    }

    public function getId()
    {
        return $this->id;
    }

    public function getName()
    {
        return $this->name;
    }

    public function setName( $name )
    {
        $this->name = $name;
    }

    public function getAddress()
    {
        return $this->address;
    }

    public function setAddress( $address )
    {
        $this->address = $address;
    }

    public function getCity()
    {
        return $this->city;
    }

    public function setCity( $city )
    {
        $this->city = $city;
    }

    public function getState()
    {
        return $this->state;
    }

    public function setState( $state )
    {
        $this->state = $state;
    }

    public function getZip()
    {
        return $this->zip;
    }

    public function setZip( $zip )
    {
        $this->zip = $zip;
    }

    public function getMeals()
    {
        return $this->meals;
    }

    public function addMeal( $meal )
    {
        $this->meals[] = $meal;
    }

    public function removeMeal( $meal )
    {
        $this->meals->removeElement( $meal );
    }

    public function jsonSerialize()
    {
        $info = array();

        $info['id']      = $this->getId();
        $info['name']    = $this->getName();
        $info['address'] = $this->getAddress();
        $info['city']    = $this->getCity();
        $info['state']   = $this->getState();
        $info['zip']     = $this->getZip();

        return $info;
    }
}
